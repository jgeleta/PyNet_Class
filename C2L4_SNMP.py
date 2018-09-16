#!/usr/bin/env python

from __future__ import print_function, unicode_literals, division
from pprint import pprint
from netmiko import Netmiko
from getpass import getpass
from ciscoconfparse import CiscoConfParse

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
import sys   # Library of variables that have strong interaction with the interpreter
import time      # 

banner = ('-' *80)     # Create a banner for use as a section separator

"""
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
prints out both the MIB2 sysName and sysDescr.
"""

import snmp_helper

sys_des = '1.3.6.1.2.1.1.1.0'
sysname = '1.3.6.1.2.1.1.5.0'


ip_addr1 = input("pynet-rtr1 IP address: ")
ip_addr2 = input("pynet-rtr2 IP address: ")
community_string = getpass(prompt="Community string: ")

pynet_rtr1 = (ip_addr1, community_string, 161)
pynet_rtr2 = (ip_addr2, community_string, 161)

for a_device in (pynet_rtr1, pynet_rtr2):
    print(banner)
    print()
    for the_oid in (sysname, sys_des):
        snmp_data = snmp_helper.snmp_get_oid(a_device, oid=the_oid)
        output = snmp_helper.snmp_extract(snmp_data)
        print(output)
        print(banner)
    print()

#EoF
