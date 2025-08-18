from . import json
from . import json_log_filepath
from .jsondata import Jsonlog
from dataclasses import asdict

def write_to_json(data):

    data_dict = asdict(data)

    try:
        with open(json_log_filepath, 'w', encoding='utf-8') as file:

            file.write(json.dumps(data_dict, indent=4))

            print("Wrote to JSON Logs")

    except Exception as e:

        print(f"Something went wrong with this operation | Error {e}")