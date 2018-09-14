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
Write a Python program using ciscoconfparse that parses this config file.
Note, this config file is not fully valid (i.e. parts of the configuration
are missing). The script should find all of the crypto map entries in the
file (lines that begin with 'crypto map CRYPTO') and for each crypto map
entry print out its children.
'''

config_file = CiscoConfParse(r'C1L8_cisco_ipsec.txt')

crypto_map = config_file.find_objects(r'crypto map CRYPTO')

# for n in crypto_map:
#    pprint(n.children)


for c_map in crypto_map:
        print()
        print(c_map.text)
        for child in c_map.children:
            print(child.text)
print()


# EoF
