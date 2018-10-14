#!/usr/bin/env python

'''
Use Jinja2 to generate the following configuration: 

--------
router ospf 40
 network 10.220.88.0 0.0.0.255 area 0
--------

The process ID, network, wildcard mask, and area should all be variables in the Jinja2 template.

Use a template directly embedded in your Python script
'''

from __future__ import print_function, unicode_literals, division
from pprint import pprint
from netmiko import Netmiko
from getpass import getpass

import os        # Allows Python to perform Operating System functions.
             # os.system - Allows Python to run commands from the Command Prompt.
import random    # Allows Python to randomly generate something, like an integer
import re        # Allows Python to perform Regular Expression searches.
import csv   # https://docs.python.org/3/library/csv.html
import jinja2    # Jinja is a template engine for the Python programming language
import yaml  # YAML is a human-readable data serialization language
import json  # JSON is an open-standard file format that uses human-readable text to transmit data objects
import telnetlib # Library the implements the Telnet protocol
import socket    # Library that will allow for socket timeouts to be coupled with try: except:
import sys       # Library of variables that have strong interaction with the interpreter
import requests  # Main Python library for HTTP and HTTPS interactions
import pynxos
import time

banner = ('-' *80)     # Create a banner for use as a section separator

ospf_config = '''
router ospf {{ process_id }}
 network {{ network }} {{ wildcard }} area {{ area }}
'''

ospf_vars = {
    'process_id': 40,
    'network': '10.220.88.0',
    'wildcard': '0.0.0.255', 
    'area': 0,
}

template = jinja2.Template(ospf_config)
output = template.render(**ospf_vars)

print(output)

# EoF
