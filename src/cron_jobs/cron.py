"""Main File for Performing the Cron Job"""

import time
import schedule

import helper
from ..logics.arxiv_extractor import ArxivExtractor

print(helper.get_time())

def task():
    arxiv_extractor = ArxivExtractor(days=60, max_results=5, data_path="data/")
    arxiv_extractor.store_data()
    print("Doing task...", helper.get_time())

# schedule.every(interval=5).seconds.do(job_func=task)
# schedule.every(interval=5).hours.do(job_func=task)

if __name__=="__main__":
    schedule.every().day.at(time_str="09:15:00").do(job_func=task)
    
    while True:
        # performs the task
        schedule.run_pending()