import typer
import Utils.logs as syslog
from Utils.hashing.hashops import run_hash_computation
from Config import _yaml_config_exist, yaml_config_filepath
from Utils.healthcheck.healthchecker import HealthChecker
import Utils.system.check_if_file_exist as system
import Utils.system.check_sys_time as systime
import typer

app = typer.Typer()

@app.callback()
def documentation():
    """
    This is a CLI Tool used to monitor the hash values of your hosted services either in the cloud or on-premise.

    documentation:
    """

@app.command()
def init():

    print(yaml_config_filepath)

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