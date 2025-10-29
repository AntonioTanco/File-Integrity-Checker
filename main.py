import typer
import time
import Utils.logs as syslog

from Automation.jobs.run_hash_job import run_hash_job
from Utils.hashing.hashops import run_hash_computation
from Config import _yaml_config_exist, yaml_config_filepath
from Utils.healthcheck.healthchecker import HealthChecker
from apscheduler.schedulers.background import BackgroundScheduler

app = typer.Typer()

automation = BackgroundScheduler()

@app.callback()
def documentation():
    """
    This is a CLI Tool used to monitor the hash values of your hosted services either in the cloud or on-premise.

    documentation:
    """
@app.command()
def automate():

    # print(yaml_config_filepath)
    # automation.add_job(run_hash_job(), trigger='interval', minutes=1)

# declearing a BackgroundScheduler() object to use within ./Automation/jobs

    automation.add_job(run_hash_job, 'interval', seconds= 30, name="hashing_task")
    print("Starting automation engine...")

    automation.start()

    print("Automation engined has started...")

    print(f"Here are the jobs found: {automation.print_jobs}")

    while True:
        time.sleep(1)

@app.command()
def init():

    print(yaml_config_filepath)

    automation.remove_all_jobs()

    if _yaml_config_exist == True:
        syslog.logging.info(f"{yaml_config_filepath} was found")
    else:
        syslog.logging.warning(f"{yaml_config_filepath} was not found")
    
@app.command()
def run_hash():
    # Run hash computation against config.yaml
    run_hash_computation()
    
@app.command()
def healthcheck():

    # creating HealthChecker Object to perform healthcheck
    healthcheck = HealthChecker(enabled=True)

    # calling perform_healthcheck() to start health check
    healthcheck.perform_healthcheck()

if __name__ == "__main__":
    app()