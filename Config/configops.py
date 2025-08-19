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

            # closes the YAML file
            # file.close()

            return data

    # Except FileNotFoundError if YAML was missing at program execution 
    except FileNotFoundError as e:

        logging.warning(f"YAML Configuration file was not found.")
        
        return e

    # returns contents of config.yaml

    # return data

def getServicesLogPaths():

    # Reading YAML Config in var for later use 
    data = readYamlConfig()

    # Checking if data['targeted_services'] is a dict
    # if isinstance(data['targeted_services'], list):

        # Storing the paths to the logs into a list
    found_services = list(data['targeted_services'])
    found_services_paths = []

    for service in found_services:
        for paths in service['service_files']:
            
            found_services_paths.append(paths)

    return found_services_paths


        # for paths in service.values():

        #     if isinstance(paths, list):
    
            #    found_services_paths.append(paths)
    # print(found_services_paths)

        # Checks values are present within YAML 
        # if found_service_log_path is not None:

        #     # Returning list of found paths for all services present in YAML
        #     return found_service_log_path
        
def getServicesName():

    # Reading YAML Config in var for later use 
    data = readYamlConfig()

    # Checking if data['targeted_services'] is a dict
    # if isinstance(data['targeted_services'], dict):

    #     # Storing the keys of data['targeted_services'] in new list var
    #     found_service_names = list(data['targeted_services'].keys())

        # Checks that the list in not Empty
        if found_service_names is not None:

            # Returns list of service names defined by User
            return found_service_names 