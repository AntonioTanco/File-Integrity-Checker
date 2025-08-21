from . import json
from . import json_log_filepath
from .jsondata import Jsonlog
from dataclasses import asdict

# function to write to JSON file
def write_to_json(data):

    #Write data as a dictionary 
    data_dict = asdict(data)

    # Try - Except block
    try:

        # Open JSON filepath | found in __init__.py
        with open(json_log_filepath, 'w', encoding='utf-8') as file:


            # Write to JSON file
            file.write(json.dumps(data_dict, indent=4))

            # Print to console that logs have been rewritten to JSON
            print("Wrote to JSON Logs")

    # Catch Exception if something went wrong with the operation
    except Exception as e:

        print(f"Something went wrong with this operation | Error {e}")


def read_json_log():

    try:

        with open(json_log_filepath, 'r', encoding='utf-8') as json:

            _json_data = json.read()

            return _json_data
        
    except Exception as e:

        print(f"{e}")
