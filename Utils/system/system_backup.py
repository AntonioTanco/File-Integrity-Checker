from pathlib import Path
from Utils.logs import logging
from Config.configops import readYamlConfig
import yaml

class SystemBackUp():

    def __init__(self, enabled: bool):
        self.enabled = enabled

    def start_backup(self, config_path: str, destination_path: str ):

        # current_config_name = Path(config_path).name
        backup_str = destination_path + "backup-config.yaml"

        backup_config_path = Path(backup_str)

        logging.info(f"this path is: {backup_config_path}")

        try:
            with backup_config_path.open('w') as backup_file:

                oldConfigData = readYamlConfig()

                yaml.safe_dump(oldConfigData, backup_file)

                logging.info(f"{backup_file.name} was created.")

                backup_file.close
            
            return True
                
        except Exception as e:

            # Print to console the Exception
            print(f"An unexpected error occurred while creating config.yaml: {e}")
        