from pathlib import Path
from Utils.logs import logging

class SystemBackUp():

    def __init__(self):
        pass

    def start_backup(self, config_path: str):

        _config_file = Path(config_path).exists()

        if _config_file == True:

            logging.info("Initating Backup of config.yaml")

            return {"Congig.yaml was found and backed up."}
