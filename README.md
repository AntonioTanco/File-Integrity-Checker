# File Integrity Checker

> [!NOTE]
> This program is meant to be a showcasing of my skills rather than a tutorial. Please review the code before cloning this repo as you should never run any code you don't understand on your system. 


<h3>Project Overview</h3>
<p>Used the hashlib Cryptography library to create a python program which will calculate the SHA256 hash value for any file you'd like to ensure the integrity of.</p>

<p>The idea is that the program allows you to append file paths to the config.yaml you'd like to keep tabs on. Every time this program is executed you'll get the hash value for those files. </p>

<h3>Project Features</h3>

- Config.yaml allows you to append any services and paths you would like to keep tabs on
- Internal System check will check if the file path exist before trying to calculate the hash

<h2>Getting Started</h2>
<h4>1. Activate Your Vitural Environment</h4>

```
python3 -venv .venv
```
<b> You may check if your vitural environment is enabled by using the command below </b>
```
pip -V
```

<h4>2. Install the required packages</h4>

```
pip install -r requipments.txt
```

<b> This will install all of the neccessary packages needed to run this project. </b>

<h4>3. Add the name of the target service and the path to any file in config.yaml.</h4>

```
# Config.yaml EXAMPLE as demonstrated in this project

targeted_services:
  Rufus install: C:\Users\smoke\Downloads\rufus-4.9.exe
```

<h4>4. Execute main.py from its root dir to output the hash value</h4>

```
# EXAMPLE of the output running from my machine given that config.yaml looks like:

targeted_services:
  Rufus install: C:\Users\smoke\Downloads\rufus-4.9.exe
```

Here's an example of what the output would look like given the Configuration shown above:

```
2025-08-16 14:51 - INFO - rufus-4.9.exe exist as a file in system
497f796e6d076d4855d697965c04626e6d3624658fce3eca82ab14f7414eede2
2025-08-16 14:51 - INFO - Calculated hashes successfully for: ['Rufus install']
```
