#!/usr/bin/env python

from __future__ import print_function, unicode_literals, division
from pprint import pprint
from netmiko import Netmiko
from getpass import getpass
from ciscoconfparse import CiscoConfParse

import os       # Allows Python to perform Operating System functions.
            # os.system   Allows Python to run commands from the Command Prompt.
import random   # Allows Python to randomly generate something, like an integer
import re       # Allows Python to perform Regular Expression searches.
import csv  # https://docs.python.org/3/library/csv.html
import jinja2   # Jinja is a template engine for the Python programming language
import yaml # YAML is a human-readable data serialization language
import json # JSON is an open-standard file format that uses human-readable text to transmit data objects

banner = ('-' *80)     # Create a banner for use as a section separator

'''
Write a Python program that creates a list. One of the elements of the list should be a dictionary
with at least two keys. Write this list out to a file using both YAML and JSON formats.
The YAML file should be in the expanded form.
'''

# Create the dictionary
my_dict = {
    'switch1': '10.0.0.1',
    'switch2': '10.0.0.2',
    'switch3': '10.0.0.3',
    'switch4': '10.0.0.4'
    }

# Create the list which also contains the dictionary
my_list = [
    my_dict,
    'hostname1',
    'hostname2',
    'hostname3',
    'hostname4'
    ]

# Create the YAML File
filename = 'C1L6.yml'
with open(filename,'w') as file:
   yaml_data = yaml.dump(my_list,file,default_flow_style=False)

# Create the JSON File
filename = 'C1L6.json'
with open(filename,'w') as file:
   json_data = json.dump(my_list,file)

# EoF
