import urllib.request
from zipfile import ZipFile
from os import system, chdir, remove
from shutil import rmtree

osc_download_url = "https://bitbucket.org/grailapp/osc/get/6a60f9376f69.zip"
osc_zip_name = "download.zip"
osc_dir_name = "grailapp-osc-6a60f9376f69"

# Download OSC module from Bitbucket
print("Downloading OSC module from Bitbucket...\n")
urllib.request.urlretrieve(osc_download_url, osc_zip_name)

# Extract OSC Module
print("Extracting OSC Module...\n")
with ZipFile(osc_zip_name) as file:
    file.extractall()

# Install the osc Python module
print("Installing 'osc' Python Module...\n")

chdir(osc_dir_name)
system("python setup.py install")
system("cd ../")
chdir("../")

# Cleanup
print("Cleaning up install files...\n")
remove(osc_zip_name)
rmtree(osc_dir_name)

# Install other requirements with pip
print("Installing other requirements with pip...\n")
system("python -m pip install -r requirements.txt")

# Done
print("\nComplete!\n")