import yaml
from pathlib import Path
from Utils.logs import logging
from dataclasses import dataclass, asdict, field
from typing import List

# Declaring name for YAML Config
yaml_config = Path('config.yaml')
yaml_config_filepath = str(yaml_config.resolve())
yaml_config_exist = bool

# Defining TargetedServiceConfig data structure for type safety
@dataclass
class TargetedServiceConfig():
    service_name: str
    service_files: List[str] = field(default_factory=list)

# Defining YAMLCONFIG data structure 
@dataclass()
class yamlconfig():
    targeted_services: List[TargetedServiceConfig]

if yaml_config.is_file():

    yaml_config_exist = True

    logging.info(f"{yaml_config} was found...")

elif yaml_config.is_file == False:

    logging.info(f"Creating {yaml_config}...")

    yaml_config.touch()

    sample_data = [TargetedServiceConfig(service_name="test_service", service_files=["SAMPLE/PATH"])]
    
    yaml_config = asdict(yamlconfig(targeted_services=sample_data))

    # Try-Except the operation of creating a new YAML Config
    try:

        # Opening a new file within the system
        with open(yaml_config, 'w') as file:

            # Creating data var to dump 'config_data' into YAML file named: YAML_FILE_NAME
            yaml.safe_dump(yaml_config, file)

            # yamlfile.write(data)

            # Logging to console the YAML file was created
            logging.info(f"{yaml_config} was created.")

            # Closing the file after it has been written to
            file.close()

    # Excepts any error that may occur when trying to create the YAML file in the event it fails
    except Exception as e:

        # Print to console the Exception
        print(f"An unexpected error occurred while creating config.yaml: {e}")
    