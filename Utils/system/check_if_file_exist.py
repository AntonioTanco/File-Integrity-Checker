from pathlib import Path
from Utils.logs import logging

def check_if_file_exist(path_to_files):

    if isinstance(path_to_files, str):
        # Perform this operation below

        path_to_check = Path(path_to_files)

        test = path_to_check.resolve()

        print(f"this is the abs path: {test}")

        if path_to_check.exists() == True:

            return True
        
        elif path_to_check.exists() == False:

            return False
    
    elif isinstance(path_to_files, list):
         
         for file in path_to_files:
              
              file_to_check = Path(file)

              file_name = file_to_check.name

              if file_to_check.is_file():
                   
                   logging.info(f"{file_name} " + "exist as a file in system")
              else:
                   logging.warning(f"{file_name} does not exist as a file in this system")
         return True


    # for file in path_to_file:

    #     log_file = Path(file)

    #     log_file_name = log_file.name

    #     if log_file.is_file():

    #         logging.info(f"{log_file_name} " + "exist as a file in system")

    #     else:

    #         logging.warning(f"{log_file_name} " + "does not exist as a file in system")

    #         return False

    # return True


