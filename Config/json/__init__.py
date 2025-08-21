from pathlib import Path
import json as json

# Create a mew folder in the defined directory
JSON_LOG_DIRECTORY = Path(r"C:\Users\smoke\Documents\File Integrity Checker\Logs")

# Creating .JSON log file 
jSON_LOG_FILENAME = "Integrity_logs.json"

# Use mkdir function to create a new folder 
JSON_LOG_DIRECTORY.mkdir(exist_ok=True)

json_log_filepath = JSON_LOG_DIRECTORY / jSON_LOG_FILENAME

if not json_log_filepath.exists():

    json_log_filepath.write_text(json.dumps({}, indent=4))

# elif json_log_filepath.exists():

    

