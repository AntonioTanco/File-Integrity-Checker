from pathlib import Path
from Utils.logs import logging

def check_if_file_exist(path_to_file: list):

    for file in path_to_file:

        log_file = Path(file)

        log_file_name = log_file.name

        if log_file.is_file():

            logging.info(f"{log_file_name} " + "exist as a file in system")

        else:

            logging.warning(f"{log_file_name} " + "does not exist as a file in system")

            return False

    return True


