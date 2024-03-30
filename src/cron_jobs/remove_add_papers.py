import os
import pandas as pd
from datetime import datetime, timedelta

def remove_old_papers(data_path, save_path, window_size) -> None:
    """Remove all the papers from the oldest day within the window size"""

    df:pd.DataFrame = pd.read_pickle(filepath_or_buffer=data_path)
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
    df.to_json(path_or_buf=save_path, orient="records", lines=True)


def add_new_papers(latest_papers_path, master_data_path) -> None:
    """Add new papers to the master data JSON file"""
    latest_papers = pd.read_pickle(filepath_or_buffer=latest_papers_path)

    # Check if the master data file already exists
    if os.path.exists(path=master_data_path):
        master_data = pd.read_json(path_or_buf=master_data_path, lines=True)
        # Concatenate the latest papers DataFrame with the existing master data
        master_data = pd.concat(objs=[master_data, latest_papers], ignore_index=True)
    else:
        # If the master data file doesn't exist, use the latest papers as the master data
        master_data = latest_papers
    master_data.to_json(path_or_buf=master_data_path, orient="records", lines=True)

remove_old_papers(data_path="../../data/master_data.json", save_path="../../data/master_data.json", window_size=365)
add_new_papers(latest_papers_path="../../data/latest_data.pkl", master_data_path="../../data/master_data.json")

