"""Main File for Performing the Cron Job"""

import schedule
import time
import os

import pandas as pd
from datetime import datetime, timedelta
# from ..logics.data_extraction import ArxivParser
from src.logics.data_extraction import ArxivParser
from src.logics.arxiv_recommender import update_vocab_with_new_data

# First install
# Download data
# run cron jobs from next day
# create vocab for recommender
# check everything is doable by poetry, for example installation and running, issue with numpy installation https://github.com/python-poetry/poetry/issues/3894
# preferences of the user
# synchronise data reloading in fastapi endpoint and updates in master data and todays data by this file
# It takes time to calculate tf-idf for 10K papers

def get_time() -> str:
    """Gets the current time and returns it as a String

            Hr:Min:Sec   D/M/Y
    Example: '19:18:15 (03/03/24)'

    """
    return time.strftime("%X (%d/%m/%y)")


def remove_old_papers(data_path, save_path, window_size) -> None:
    """Remove all the papers from the oldest day within the window size"""

    df: pd.DataFrame = pd.read_pickle(data_path)
    df["published_date"] = pd.to_datetime(arg=df['published_date'])

    # Calculate the cutoff date
    today = datetime.today().date()
    cutoff_date = (today - timedelta(days=window_size + 1)).strftime("%Y-%m-%d")

    # Convert cutoff_date to datetime
    cutoff_date = pd.to_datetime(arg=cutoff_date)

    # Find papers to remove
    papers_to_remove = df[df['published_date'] <= cutoff_date]

    # Remove the old papers
    df = df[~df.index.isin(values=papers_to_remove.index)]

    # Convert published_date column to string in the desired format
    df['published_date'] = df['published_date'].dt.strftime(date_format='%Y-%m-%d')

    # Save the updated dataframe
    df.to_pickle(save_path)


def add_new_papers(latest_papers_path, master_data_path) -> None:
    """Add new papers to the master data JSON file"""
    latest_papers = pd.read_pickle(latest_papers_path)

    # Check if the master data file already exists
    if os.path.exists(path=master_data_path):
        master_data = pd.read_pickle(master_data_path)
        # Concatenate the latest papers DataFrame with the existing master data
        master_data = pd.concat(objs=[master_data, latest_papers], ignore_index=True)
    else:
        # If the master data file doesn't exist, use the latest papers as the master data
        master_data = latest_papers
    master_data.to_pickle(master_data_path)


TOTAL_PAPERS_WINDOW_SIZE = 1900

def download_todays_paper_task() -> None:
    parser = ArxivParser()
    parser.store_data(save_file_name="todays_data.pkl", max_results=10000, days=2)
    print("Doing task...", get_time())


def remove_old_papers_add_new_papers() -> None:
    print("Doing task...", get_time())
    add_new_papers(latest_papers_path="data/todays_data.pkl", master_data_path="data/master_data.pkl")
    remove_old_papers(data_path="data/master_data.pkl", save_path="data/master_data.pkl",
                      window_size=TOTAL_PAPERS_WINDOW_SIZE)

    update_vocab_with_new_data("data/master_data.pkl")


if __name__=="__main__":
    # schedule.every().day.at(time_str="23:58:45").do(job_func=download_todays_paper_task)
    # schedule.every().day.at(time_str="23:59:59").do(job_func=remove_old_papers_add_new_papers)
    # # schedule.every(interval=5).seconds.do(job_func=task)
    #
    # while True:
    #     # performs the task
    #     schedule.run_pending()

    parser = ArxivParser()
    parser.store_data(save_file_name="todays_data.pkl", max_results=10000, days=16)
    add_new_papers(latest_papers_path="data/todays_data.pkl", master_data_path="data/master_data.pkl")
    remove_old_papers(data_path="data/master_data.pkl", save_path="data/master_data.pkl", window_size=1)

    update_vocab_with_new_data("data/master_data.pkl")

    # download_todays_paper_task()
    # remove_old_papers_add_new_papers()
