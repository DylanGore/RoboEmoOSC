# RoboEmoOSC

A Python script designed to receive messages over OSC corresponding to the emotional state of a robotic lamp and play a sound file from a set of files based on that emotion.

## Usage

To use simply run:

```python oscserver.py```

Optional Arguments:

- ```--ip IP_ADDRESS``` - IP address for the OSC server to listen on (_Default: 0.0.0.0_)

- ```--port PORT_NUMBER``` - Port address for the OSC server to listen on (_Default: 5000_)

## Installation

Installation is handled by the ```install.py``` script as the osc module used is not available via pip. This script will download the OSC module from Bitbucket, extract and install it and will then install all pip requirements listed in ```requirements.txt```.

## Requirements

- [OSC](https://bitbucket.org/grailapp/osc/src/default/)
- [playsound](https://pypi.org/project/playsound/)