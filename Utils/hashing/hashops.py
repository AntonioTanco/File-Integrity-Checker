# import hashlib
# import sys

# from Config import yaml
from Utils.logs import logging as syslog
import hashlib 

#Defining the buff size used for file operations
BUFF_SIZE = 65536

def getFilesHash(logs_path: list):

    if isinstance(logs_path, list):

        for logs in logs_path:

             # Re-initalizing hash for use in the script
            hasher = hashlib.sha256()
            # print(f"{logs}")
            with open(logs, "rb") as f:

                while True:

                    data = f.read(BUFF_SIZE)

                    if not data:

                        break

                    hasher.update(data)

                print(hasher.hexdigest())
    
    elif logs_path is None:

        syslog.critical("No valid paths listed in YAML Config")

        

def getListOfHashes(files):

    getFilesHash(files)