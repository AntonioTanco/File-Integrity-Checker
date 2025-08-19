# File Integrity Checker

> [!NOTE]
> This program is meant to be a showcasing of my skills rather than a tutorial. Please review the code before cloning this repo as you should never run any code you don't understand on your system. 


<h3>Project Overview</h3>
<p>Used the hashlib Cryptography library to create a python program which will calculate the SHA256 hash value for any file you'd like to ensure the integrity of.</p>

<p>The idea is that the program allows you to append file paths to the config.yaml you'd like to keep tabs on. Every time this program is executed you'll get the hash value for those files. </p>

<h3>Project Features</h3>

- 📝 Config.yaml allows you to append any services and paths you would like to keep tabs on
  - Read more about [Config.yaml](##About-Config.yaml) below
- 🔍 Internal System check will check if the file path exist before trying to calculate the hash
  - Read more about the [Internal System Check](##About-Config.yaml) below
- 📦 Out-of-Box cross platform support with MacOS, Windows and Linux systems
- 🎉 Output gets parsed into a readable JSON File called: Integrity_logs.json

<h4>Python Libraries Used:</h4>

- Hasblib: https://docs.python.org/3/library/hashlib.html

- Pathlib: https://docs.python.org/3/library/pathlib.html
  
- PyYaml: https://pyyaml.org/wiki/PyYAMLDocumentation
</br>
<h2>Getting Started: Windows</h2>
<h4>1. Clone the repo into a directory of your choice an activate your Virtural Environment</h4>

```
python3 -m venv .venv
```

<b> After activating your Virtual Environment ensure you have the latest version of pip3 installed. </b>
```
pip3 --version

&

# This command will install the latest version of pip

python3 -m pip install --upgrade pip 
```

<h4>2. Install the required packages</h4>

```
# This installs the packages required to run this program using requirements.txt to install of the required dependencies 

pip install -r requipments.txt
```

<p>NOTE: This will install all of the neccessary packages needed to run this project. </p>

<h4>3. Modify Config.yaml to include the of the target service and the path to any file or log you'd like to generate the SHA256 hash for.</h4>

```
# Config.yaml as demonstrated for the 'Getting Started' Example | OS: Windows 10
# Feel free to modify this Config.yaml to your liking

targeted_services:
  Rufus install: C:\Users\smoke\Downloads\rufus-4.9.exe
```

<h4>4. Execute main.py from its root dir to output the hash value</h4>

```
python3 main.py
```

```
# EXAMPLE of the output running from a Windows 10 machine given the config shown:

targeted_services:
  Rufus install: C:\Users\smoke\Downloads\rufus-4.9.exe
```

Here's an example of what the output would look like given the Configuration shown above:

```
2025-08-16 14:51 - INFO - rufus-4.9.exe exist as a file in system
497f796e6d076d4855d697965c04626e6d3624658fce3eca82ab14f7414eede2
2025-08-16 14:51 - INFO - Calculated hashes successfully for: ['Rufus install']
```

<h2>Getting Started: MacOS</h2>

<h4>1. Clone the repo into a directory of your choice an activate your Virtural Environment</h4>

```
python3 -m venv .venv
```

<b> After activating your Virtual Environment ensure you have the latest version of pip3 installed. </b>
```
pip3 --version

&

# This command will install the latest version of pip

python3 -m pip install --upgrade pip 
```


<h4>2. Install the required packages</h4>

```
# This installs the packages required to run this program using requirements.txt to install of the required dependencies 

pip install -r requipments.txt
```

<p>NOTE: This will install all of the neccessary packages needed to run this project. </p>

<h4>3. Modify Config.yaml to include the of the target service and the path to any file or log you'd like to generate the SHA256 hash for.</h4>

```
# Config.yaml as demonstrated for the 'Getting Started' Example | OS: MacOS
# Feel free to modify this Config.yaml to your liking

targeted_services:
  service_name: /Users/admin/Documents/File Integrity Checker/File-Integrity-Checker/test.txt
  Proton Install: /Users/admin/Downloads/ProtonDrive-1.16.0.dmg
```

<img width="887" height="158" alt="Screenshot 2025-08-17 at 4 25 23 PM" src="https://github.com/user-attachments/assets/2f08705b-2cce-4a0e-8503-3bc88e7fbc97" />

<h4>4. Execute main.py from its root dir to output the hash value</h4>

```
python3 main.py
```

```
# EXAMPLE of the output running from my MacOS machice given the config.yaml shown

targeted_services:
  service_name: /Users/admin/Documents/File Integrity Checker/File-Integrity-Checker/test.txt
  Proton Install: /Users/admin/Downloads/ProtonDrive-1.16.0.dmg
```

Here's an example of what the output would look like given the Configuration shown above:

```
2025-08-17 16:23 - INFO - test.txt exist as a file in system
2025-08-17 16:23 - INFO - ProtonDrive-1.16.0.dmg exist as a file in system
e360f6bd84402ee941de1b3e7956f4cc843766a83e312b83389bbdbdb8946b78
7276fa2c6a040969a74958ba54c671792232b69a0768359bf80ff378b607e43c
2025-08-17 16:23 - INFO - Calculated hashes successfully for: ['service_name', 'Proton Install']
```

<img width="881" height="76" alt="Screenshot 2025-08-17 at 4 27 59 PM" src="https://github.com/user-attachments/assets/70e52a3d-8dcf-478b-b46c-956ca923ba7a" />

## About Config.yaml

The ability to configure a program to suite your needs was a big reason why I included a yaml config within this project. Most File Integrity Checkers tends to be lacking in features such as this one and because I wanted to create one that is Cross-platform there was an even greater responsiblity not to hardcode anything that pretains to where this program might live on a system no matter what Operating System it may be. 

This means I had to account for how this program interacts with the filesystem as a whole. It was a conscious design decision to allow the user to append file paths to a Config.yaml it's type safe and easy to modify per system rather then leaving that part up to the program itself. 

This program uses the paths present in the Config.yaml to then run an internal system check to ensure that those files actually exist with the file system. Let's first talk about Config.yaml's structure and how it ties into the rest of the program. 

<h3>Config.yaml</h3>
<p>The data you see here is what will first get generated once you execute the program for the first time. This data structure comes from the internal dataclasses in Config/__init__.py.

Config/__init__.py plays a critical role as to how this program functions allowing Config to serve as an importable package throughout the program but also allows for us to initialize where Config.yaml will live relative to the program and what data structure it should have upon first import.</p>

```
targeted_services:
- service_files:
  - SAMPLE/PATH
  service_name: test_service
```

'targeted_services:' is defined by these two dataclass Objects defined below.

```
@dataclass
class TargetedServiceConfig():
    service_name: str
    service_files: List[str] = field(default_factory=list)

# Defining YAMLCONFIG data structure 
@dataclass()
class yamlconfig():
    targeted_services: List[TargetedServiceConfig]
```
You'll noticed that this yaml structure is really just a list of the TargetedServiceConfig() dataclass which takes a _service_name_ (this being the name of whatever you want to watch over) and takes a list of strings as _service_files_ (this being where you'd associate file paths to a particular _service_name_). 

Once you've entered or populated Config.yaml with how every many Targeted Service Configurations you'd like, the internal system check will then be responsible for checking if those files exist within the host filesystem.

## About The Internal System Check

Since I wanted this project to be Cross-platform, I needed a way to interact with the file system using the data from Config.yaml in a way that was agnostic to the underlying platform it was installed on. This is where I choosed to use Python's internal Pathlib module for this case.

Pathlib takes an Object-oriented approach to handling file systems paths since **Path** automatically adapts to the conventions of the underlying platform operating system eliminating the need to develop a platform-specific component to handle the logic for path manipulation. 

You may read more about Pathlib here: https://docs.python.org/3/library/pathlib.html

<h3>System/__init__.py.</h3>

This information gets processed immediately when the system module is imported in main.py. This is important as this information is imperative to any program that intends to run Cross-platform. Meaning if a particular bug were to be found, the fix can be implemented and replicated in the exact same environment if need be. 

This information is printed to console so the end-user can forward this information as a Github issue and it can be addressed in a seperate branch. 

```
#System/__init__.py

import platform

UNAME_INFO = platform.uname()
print(f"System: {UNAME_INFO.system}")
print(f"Node: {UNAME_INFO.node}")
print(f"Release: {UNAME_INFO.release}")
print(f"Version: {UNAME_INFO.version}")
print(f"Machine: {UNAME_INFO.machine}")
print(f"Processor: {UNAME_INFO.processor}")

def get_nodes_name():
    return UNAME_INFO.node
```

The logic that handles if a file exist within the file systems comes from System/check_if_file_exist.py. This is where the logic built using the Path module can be found. Here's a breakdown on how this work pertaining to the rest of the program.

```
from pathlib import Path
from Utils.logs import logging

def check_if_file_exist(path_to_file: list):

    for file in path_to_file:

        log_file = Path(file)

        log_file_name = log_file.name

        if log_file.is_file():

            logging.info(f"{log_file_name} " + "exist as a file in system")

        else:

            logging.warning(f"{log_file_name} " + "does not exist as a file in system")

            return False

    return True

```

In main.py before any SHA256 computations are made we of course want to check if all of these files found in Config.yaml actually exist. To achieve this logic check_if_file_exist(path_to_file: list) function is used in main.py and it's Boolean output is stored in a variable named: _file_path_exist_ for use in a simple if statement. 

<h4>main.py</h4>

```
import Utils.hashing.hashops as hash
import Config.configops as config
import Config.json.jsondata as _json
import Config.json.jsonops as log
import Utils.logs as syslog
from Utils.system import get_nodes_name
import Utils.system.check_if_file_exist as system
# use getServicesLogPaths() from config to store a list of paths to files from CONFIG.YAML
TARGETED_LOG_FILE = config.getServicesLogPaths()

# use getServicesName() from config to store a list of paths to files from CONFIG.YAML
TARGETED_SERVICE_NAMES = config.getServicesName()

# run check on TARGETED_LOG_FILE to see if files exist within the system
file_path_exist = system.check_if_file_exist(TARGETED_LOG_FILE)

# Creating function to run hash computation on program execution
def run_hash_computation():

    config.readYamlConfig()
    # Checking if files listed in YAML Config exist within the system
    if file_path_exist == True:
        
    #     # calculate and return hash of all the files present in YAML Config
        cal_hash = hash.getFilesHash(TARGETED_LOG_FILE)

        operations = _json.Jsonlog(hostname=get_nodes_name(), 
                                   targeted_paths=TARGETED_LOG_FILE, 
                                   targeted_services=TARGETED_SERVICE_NAMES, 
                                   hashes_generated=cal_hash)

        log.write_to_json(operations)

    print("test")

        # print to console - hashes were successfully calculated for the targeted services after hashes were calculated
        # syslog.logging.info(f"Calculated hashes successfully for: {TARGETED_SERVICE_NAMES}")

if __name__ == "__main__":
    run_hash_computation()
```

Step 1. file_path_exist = system.check_if_file_exist(TARGETED_LOG_FILE) gets called at runtime whenever this program is executed. TARGETED_LOG_FILE is a static variable that is just a list of ALL file paths that were appended to Config.yaml. That operation happens within the configops class imported from the Config module located at Config/configops.py.

<p>Here's a look at config.getServicesLogPaths()</p>

```
def getServicesLogPaths():

    # Reading YAML Config in var for later use 
    data = readYamlConfig()

    # Checking if data['targeted_services'] is a dict
    # if isinstance(data['targeted_services'], list):

    # Storing the paths to the logs into a list
    found_services = list(data['targeted_services'])

    # Creating an empty list to append file paths to
    found_services_paths = []

    for service in found_services:
        for paths in service['service_files']:
            
            found_services_paths.append(paths)

    # Return a list of strings (file paths) found in Config.yaml
    return found_services_paths
```

Step 2. config.getServicesLogPaths() will perform a list comprehension operation against the data read from Config.yaml stored in the local data variable and will return a list of strings of all of the _service_files_ found within the file system.  

Step 3. main.py performs an if statement check on whether or not the variable _file_path_exist__ is True. if the Internal system check finds that all of the files do exist this check will pass and will start the SH265 hash computation. The module Utils.hashing is where we import the hashing function getFilesHash() which lives in hashops.py located at Utils/hashing/hashops.py

<p>Here is a look at the getFilesHash() function</p>

```
def getFilesHash(logs_path: list):

    # Checking if logs+path passed into function is of type: list
    if isinstance(logs_path, list):

        # Creating an empty list to append hashes generated by this function later on

        list_of_hashes = []

        # Iterating through each log in logs_path
        for logs in logs_path:

             # Re-initalizing hash for use in the script
            hasher = hashlib.sha256()

            # opening up each log
            with open(logs, "rb") as f:

                while True:
                    
                    # Reading data according to BUFF_SIZE
                    data = f.read(BUFF_SIZE)

                    if not data:

                        break
                    
                    # data the hash stored in hasher Object
                    hasher.update(data)
                
                list_of_hashes.append(hasher.hexdigest())
            
        return list_of_hashes
    
    elif logs_path is None:

        syslog.critical("No valid paths listed in YAML Config")
```


<p>getFilesHash() accepts a list of strings as an input in this case the list we want to perform this operation on would be **TARGETED_LOG_FILE** as found in main.py which is already a list of file_paths ready for processing. A simple for loop iterates through each file in the provided list and will open up the file in 'read/binary' mode and read bytes of the the file according to the arbitrary BUFF_SIZE variable declared in this class. We reinitizing a new SHA 265 hashlib object to ensure the correct hash is produced through every iteration of the for loop. Each iteration gets appended to an empty list _list_of_hashes_ which gets returned as soon as the for loop operation is done. </p>

Step 4. simply open up the JSON file: Integrity_logs.json located in the folder .Logs/ - this is where main.py will write the output of the operation to you in a json format that is readable. 

<p>Here is an example of what Integrity_logs.json looks like against the test.txt file in my projects directory.</p>

```
{
    "hostname": "WINDOWS-TEST-SYS",
    "targeted_services": [
        "test_service"
    ],
    "targeted_paths": [
        "C:\\Users\\smoke\\Documents\\File Integrity Checker\\test.txt"
    ],
    "hashes_generated": [
        "e360f6bd84402ee941de1b3e7956f4cc843766a83e312b83389bbdbdb8946b78"
    ]
}

```
