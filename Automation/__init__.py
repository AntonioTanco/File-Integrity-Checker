import schedule
from Utils.hashing.hashops import run_hash_computation
import time


# Defining the run_hash_job func
def run_hash_job():

    # Calling upon the run_hash_computation function to perform hashing operation
    run_hash_computation()

schedule.every(5).minutes.do(run_hash_job())

while True:

    schedule.run_pending()
    time.sleep(1)