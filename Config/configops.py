import Config
from Utils.logs import logging
import Utils.logs as syslog

def readYamlConfig():

    # Open config.yaml in read mode

    # Try-catch when opening 'config.yaml'
    try:
        with open('config.yaml', 'r') as file:

            # Load the YAML content into data var
            
            data = Config.yaml.safe_load(file)

            # print(data)

            # closes the YAML file
            file.close()

            return data

    # Except FileNotFoundError if YAML was missing at program execution 
    except FileNotFoundError as e:

        logging.warning(f"YAML Configuration file was not found.")
        
        return e

def getServicesLogPaths():

    # Reading YAML Config in var for later use 
    data = readYamlConfig()

    found_services = list(data['targeted_services'])
    found_services_paths = []

    for service in found_services:
        for paths in service['service_files']:
            
            found_services_paths.append(paths)

    return found_services_paths
        
def getServicesName():

    # Reading YAML Config in var for later use 
    data = readYamlConfig()

    found_services = list(data['targeted_services'])
    found_services_names = []

    for service in found_services:
        # for service_names in service['service_name']:
        found_services_names.append(service['service_name'])

    return found_services_names
