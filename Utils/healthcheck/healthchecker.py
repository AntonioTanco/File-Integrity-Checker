from pathlib import Path
from Utils.system import check_if_file_exist
from Config import yaml_config_filepath

class HealthChecker():

    def __init__(self, enabled: bool):
        self.enabled = enabled
    
    def perform_healthcheck(self):

        if self.enabled == False:
            pass

        elif self.enabled == True:

            print("[Health Check] - Checking if config.yaml exist...")

            if yaml_config_filepath.exists():

                print("[Health Check] - config.yaml does exist")
            else: 
                print("[Health Check] - config.yaml does not exist")
            
            
