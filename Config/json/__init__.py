from pathlib import Path
import json

# Create a mew folder in the defined directory
json_log_directory = Path(r"C:\Users\smoke\Documents\File Integrity Checker\Logs")

# Creating .JSON log file 
json_log_filename = "Integrity_logs.json"

# Use mkdir function to create a new folder 
json_log_directory.mkdir(exist_ok=True)

json_log_filepath = json_log_directory / json_log_filename

if not json_log_filepath.exists():

    json_log_filepath.write_text(json.dumps({"Hello": "JSON"}, indent=4))

