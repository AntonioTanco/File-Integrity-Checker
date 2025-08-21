from . import json
from . import JSON_LOG_DIRECTORY
from .jsondata import Jsonlog
from dataclasses import asdict

# function to write to JSON file
def write_to_json(data):

    #Write data as a dictionary 
    data_dict = asdict(data)

    # Try - Except block
    try:

        # Open JSON filepath | found in __init__.py
        with open(JSON_LOG_DIRECTORY, 'w', encoding='utf-8') as file:


            # Write to JSON file
            file.write(json.dumps(data_dict, indent=4))

            # Print to console that logs have been rewritten to JSON
            print("Wrote to JSON Logs")

    # Catch Exception if something went wrong with the operation
    except Exception as e:

        print(f"Something went wrong with this operation | Error {e}")

# function to read JSON file
def read_json_log():

    # Try - Except block for open json file operation
    try:

        # Open JSON using JSON_LOG_DIR var as json
        with open(JSON_LOG_DIRECTORY, 'r', encoding='utf-8') as json:
            
            # store json data in _json_data to return
            _json_data = json.read()

            # return _json_data
            return _json_data
        
    except Exception as e:

        print(f"{e}")
