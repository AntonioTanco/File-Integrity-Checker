# File Integrity Checker

> [!NOTE]
> This program is meant to be a showcasing of my skills rather than a tutorial. Please review the code before cloning this repo as you should never run any code you don't understand on your system. 


<h3>Project Overview</h3>
<p>Used the hashlib Cryptography library to create a python program which will calculate the SHA256 hash value for any file you'd like to ensure the integrity of.</p>

<p>The idea is that the program allows you to append file paths to the config.yaml you'd like to keep tabs on. Every time this program is executed you'll get the hash value for those files. </p>

<h3>Project Features</h3>

- Config.yaml allows you to append any services and paths you would like to keep tabs on
- Internal System check will check if the file path exist before trying to calculate the hash
- Out-of-Box cross platform support with MacOS, Windows and Linux systems

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

