#!/usr/bin/env python

'''
Use the pynxos library and NX-API to retrieve the output of 'show ip route vrf management'
from the nxos1 switch. Parse the returned data structure and from this, retrieve the next
hop for the default route. Print this to standard output.
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

raw_route_table = nxos1.show('show ip route vrf management')
pprint(raw_route_table)

print()
print(banner)
print()


route_table = raw_route_table['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']['TABLE_prefix']['ROW_prefix']
pprint(route_table)

print()
print(banner)
print()

for routing_entry in route_table:
    if routing_entry['ipprefix'] == '0.0.0.0/0':
        pprint(routing_entry.values())

next_hop = route_table['TABLE_prefix']['ROW_prefix']
next_hop = next_hop['ipnexthop']

print()
print('The gateway for the default route is {}'.format(next_hop))

# EoF
