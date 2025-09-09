from pathlib import Path
import json as json

from .jsondata import JsonLogData
from dataclasses import asdict

# Create a mew folder in the defined directory
json_log_directory = Path(r"C:\Users\smoke\Documents\File Integrity Checker\Logs")

# Creating .JSON log file 
jSON_LOG_FILENAME = "Integrity_logs.json"

# Use mkdir function to create a new folder 
json_log_directory.mkdir(exist_ok=True)

json_log_filepath = json_log_directory / jSON_LOG_FILENAME

if not json_log_filepath.exists():

    new_json_data = JsonLogData()

    json_log_filepath.write_text(json.dumps(asdict(new_json_data), indent=4))

# elif json_log_filepath.exists():

    

