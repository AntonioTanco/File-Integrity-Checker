import yaml
import os
from Utils.logs import logging
from dataclasses import dataclass, asdict
from typing import List

# Declaring name for YAML Config
YAML_FILE_NAME = 'config.yaml'

# OLD YAML IMPLEMENTATION
# Delaring config_data
# config_data = {
#     # config.yaml
#     # sample-syntax 
#     #"targeted_services":
#     #   "sample_service_name": path_to_service_logs (str)
#     "targeted_services":
#     {
#         "service_name": r"C:\Users\smoke\Documents\File Integrity Checker\test.txt"
#     }
# }

# Declearing a new dataclasses to structure config.yaml

# Defining TargetedServiceConfig data structure for type safety
@dataclass
class TargetedServiceConfig():
    service_name: str
    service_files: List[str]

# Defining YAMLCONFIG data structure 
@dataclass
class YAMLCONFIG():
    targeted_services: List[TargetedServiceConfig]

# Check if YAML Config does not exist
if not os.path.exists(YAML_FILE_NAME):
    
    # Try-Except the operation of creating a new YAML Config
    try:

        # Opening a new file within the system
        with open(YAML_FILE_NAME, 'w') as yamlfile:

            # Creating data var to dump 'config_data' into YAML file named: YAML_FILE_NAME
            data = yaml.dump(config_data, yamlfile, default_flow_style=False)

            # Logging to console the YAML file was created
            logging.INFO(f"{yamlfile.name()} was created.")

            # Closing the file after it has been written to
            yamlfile.close()

    # Excepts any error that may occur when trying to create the YAML file in the event it fails
    except Exception as e:

        # Print to console the Exception
        print(f"An unexpected error occurred while creating config.yaml: {e}")
    