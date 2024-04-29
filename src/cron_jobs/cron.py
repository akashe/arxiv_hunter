"""Main File for Performing the Cron Job"""

import time
import schedule

import helper
from ..logics.data_extraction import ArxivParser

print(helper.get_time())

# First install
# Download data
# create vocab for recommender
# check everything is doable by poetry, for example installation and running, issue with numpy installation https://github.com/python-poetry/poetry/issues/3894
# preferences of the user
# add

def task() -> None:
    parser = ArxivParser()
    parser.store_data(save_file_name="../../data/latest_data.pkl",max_results=1000, days=1)
    # print("Doing task...", helper.get_time())

# schedule.every(interval=5).seconds.do(job_func=task)
# schedule.every(interval=5).hours.do(job_func=task)

if __name__=="__main__":
    schedule.every().day.at(time_str="14:22:00").do(job_func=task)
    # schedule.every(interval=5).seconds.do(job_func=task)
    
    while True:
        # performs the task
        schedule.run_pending()