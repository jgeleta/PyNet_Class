#!/usr/bin/env python

'''
Use the pynxos library to create an NX-API connection to both nxos1.twb-tech.com
and to nxos2.twb-tech.com. Use the pynxos 'show' method to retrieve 'show hostname'
from each of the devices. Print this show hostname output to standard output.
'''

from __future__ import print_function, unicode_literals, division
from pprint import pprint
from netmiko import Netmiko
from getpass import getpass
from pynxos.device import Device

import os        # Allows Python to perform Operating System functions.
             # os.system   Allows Python to run commands from the Command Prompt.
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
# import pynxos
import time


banner = ('-' *80)     # Create a banner for use as a section separator

# Turn off SSL warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nxos1 = Device(host='nxos1.twb-tech.com',
    username='pyclass',
    password='88newclass',
    transport='https',
    port=8443)

nxos2 = Device(host='nxos1.twb-tech.com',
    username='pyclass',
    password='88newclass',
    transport='https',
    port=8443)

device_list = [nxos1, nxos2]

for host in device_list:
    print()
    print(host.show('show hostname'))

# EoF
