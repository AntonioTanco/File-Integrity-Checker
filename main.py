import typer
import Utils.logs as syslog
import time

from typing_extensions import Annotated
from Utils.system.system_threads import start_hash_thread
from Utils.system.system_backup import SystemBackUp

from Config import yaml_config_exist, yaml_config_filepath
from Config.configops import readYamlConfig
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

        print("Starting automation engine...")

        automation.add_job(start_hash_thread, 'interval', seconds= 30, name="hashing_task")

        automation.start()

        print("Automation engined has started...")

        print(f"Here are the jobs found: {automation.print_jobs}")

        try:
            while start_hash_thread != False:
                time.sleep(1)  # Simulate some work or delay
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt detected. Exiting loop.")
            # You can add any cleanup code here before the program potentially exits or continues
        finally:
            print("Program execution finished.")

@app.command()
def init():

    print(yaml_config_filepath)

    automation.remove_all_jobs()

    if  yaml_config_exist == True:
        syslog.logging.info(f"{yaml_config_filepath} was found")
    else:
        syslog.logging.warning(f"{yaml_config_filepath} was not found")
    
@app.command()
def run_hash():
    # Run hash computation against config.yaml
    start_hash_thread()
    
@app.command()
def healthcheck():

    # creating HealthChecker Object to perform healthcheck
    healthcheck = HealthChecker(enabled=True)

    # calling perform_healthcheck() to start health check
    healthcheck.perform_healthcheck()

@app.command()
def backup(path: Annotated[str, typer.Argument()]):

    # creating SystemBackUp Object
    backup = SystemBackUp(enabled=True)

    # calling start_backup() to perform backup of config.yaml
    status = backup.start_backup(yaml_config_filepath, path)

    if status == True:

        syslog.logging.info("The backup was successful")

    print(readYamlConfig())
if __name__ == "__main__":
    app()