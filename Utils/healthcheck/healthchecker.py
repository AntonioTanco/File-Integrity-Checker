from Config import yaml_config_exist

class HealthChecker():

    def __init__(self, enabled: bool):
        self.enabled = enabled
    
    def perform_healthcheck(self):

        if self.enabled == False:
            pass

        elif self.enabled == True:

            print("[Health Check] - Checking if config.yaml exist...")

            if yaml_config_exist == True:

                print("[Health Check] - config.yaml does exist")
            else: 
                print("[Health Check] - config.yaml does not exist")
            
            
