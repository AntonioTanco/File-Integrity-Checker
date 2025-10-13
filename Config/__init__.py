import yaml
from pathlib import Path
from Utils.logs import logging
from dataclasses import dataclass, asdict, field
from typing import List

# Declaring name for YAML Config
YAML_FILE_NAME = 'config.yaml'

# Defining TargetedServiceConfig data structure for type safety
@dataclass
class TargetedServiceConfig():
    service_name: str
    service_files: List[str] = field(default_factory=list)

# Defining YAMLCONFIG data structure 
@dataclass()
class yamlconfig():
    targeted_services: List[TargetedServiceConfig]

# Check if YAML Config does not exist
if not os.path.exists(YAML_FILE_NAME):

    sample_data = [TargetedServiceConfig(service_name="test_service", service_files=["SAMPLE/PATH"])]

    
    
    yaml_config = asdict(yamlconfig(targeted_services=sample_data))

    # Try-Except the operation of creating a new YAML Config
    try:

        # Opening a new file within the system
        with open(YAML_FILE_NAME, 'w') as file:

            # Creating data var to dump 'config_data' into YAML file named: YAML_FILE_NAME
            yaml.safe_dump(yaml_config, file)

            # yamlfile.write(data)

            # Logging to console the YAML file was created
            logging.info(f"{YAML_FILE_NAME} was created.")

            # Closing the file after it has been written to
            file.close()

    # Excepts any error that may occur when trying to create the YAML file in the event it fails
    except Exception as e:

        # Print to console the Exception
        print(f"An unexpected error occurred while creating config.yaml: {e}")
    