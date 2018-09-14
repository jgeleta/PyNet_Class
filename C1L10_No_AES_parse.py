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
Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name).
Print these entries and their corresponding transform set name.
'''

config_file = CiscoConfParse(r'C1L8_cisco_ipsec.txt')

no_AES = config_file.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES')

print()
print('Non-AES Entries with their Transform Sets')
for n in no_AES:
    print(n.text)
    for xform in n.children:
        if 'transform-set' in xform.text:
            print(xform.text)

print()

# EoF
