"""Main File for Performing the Cron Job"""

import time
import schedule

import helper
from ..logics.data_extraction import ArxivParser

print(helper.get_time())

def task() -> None:
    parser = ArxivParser()
    parser.store_data(max_results=1000, days=1)
    # print("Doing task...", helper.get_time())

# schedule.every(interval=5).seconds.do(job_func=task)
# schedule.every(interval=5).hours.do(job_func=task)

if __name__=="__main__":
    schedule.every().day.at(time_str="14:22:00").do(job_func=task)
    # schedule.every(interval=5).seconds.do(job_func=task)
    
    while True:
        # performs the task
        schedule.run_pending()