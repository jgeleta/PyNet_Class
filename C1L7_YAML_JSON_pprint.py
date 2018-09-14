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
Write a Python program that reads both the YAML file and the JSON file created in
exercise 6 and pretty prints the data structure that is returned.
'''

# Read in the YAML File
with open('C1L6.yml') as file:
    output = yaml.load(file)
print()
print(banner)
print('These are the contents of the YAML File')
pprint(output)
print(banner)

# Read in the JSON File
with open('C1L6.json') as file:
    output = json.load(file)
print()
print(banner)
print('These are the contents of the JSON File')
pprint(output)
print(banner)

# EoF
