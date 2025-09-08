from . import json
from . import json_log_filepath
from .jsondata import JsonLogData, Jsonlog
from dataclasses import asdict

# function to write to JSON file
def write_to_json(data):

    # Creating a new list var to store Jsonlog Objects in
    list_of_entries = []

    # Checking if the data passing into the func is an instance of Jsonlog
    if isinstance(data, Jsonlog):

        # Appending the data past in the list var
        list_of_entries.append(data)

        # Check if read_json_log is not None type
        if read_json_log != None:
            
            # Read the data stored within Integrity_logs.json
            current_json_data = read_json_log()

            # Iterating through current_json_data['hashing_operations'] to convert dicts into JsonLog Objects
            for entries in current_json_data['hashing_operations']:

                # Coverting each entry to a JsonLog Object and storing it in var
                current_data_entries = Jsonlog(**entries)

                # Appending each entry to a list of JsonLog Objects
                list_of_entries.append(current_data_entries)

            try:
                with open(json_log_filepath, 'w', encoding='utf-8') as file:

                    latest_data = asdict(JsonLogData(list_of_entries))

                    # print(latest_data)

                    # file.write(json.dumps(latest_data, indent=4))

                    json.dump(latest_data, file, indent=4)

                    file.close()

                    # json.dump(latest_data, file, indent=4)
            except Exception as e:

                print(f"Error when writing to JSON Log file | Error {e}")

def read_json_log():

    # Try - Except block for open json file operation
    try:
        # Open JSON using JSON_LOG_DIR var as json
        with open(json_log_filepath, 'r', encoding='utf-8') as file:

            # store json data in _json_data to return
            _json_data = json.load(file)

            if _json_data != None:

                json_data = JsonLogData(**_json_data)

                if isinstance(json_data, JsonLogData):

                    json_data = asdict(json_data)

                    return json_data
        
    except Exception as e:

        print(f"{e}")

def json_log_entry(uuid: str):

    json_data = read_json_log()

    for entry in json_data['hashing_operations']:

        if entry['UUID'] == uuid:

            print(f"{entry['UUID']} was found")
            
            return entry