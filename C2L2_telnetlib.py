#!/usr/bin/env python

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

'''
Write a script that connects using telnet to the pynet-rtr1 router.
Execute the 'show ip int brief' command on the router and return the output.

You should be able to do this by using the following items: 

telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
net_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
net_conn.read_very_eager()
net_conn.write(<command> + '\n')
net_conn.close()
'''

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def write_bytes(out_data):
    """
    Write Python2 and Python3 compatible byte stream.
    It ensures that the unicode in the program is always encoded into a UTF-8 byte stream
    in the proper way (when bytes are written out to the network). Or worded another way,
    Unicode in the program is in the idealized unicode code points, and when you write it
    out to the network it needs to be represented a certain way (encoded).
    """
    if sys.version_info[0] >= 3:
        if isinstance(out_data, type(u'')):
            return out_data.encode('utf-8')
        elif isinstance(out_data, type(b'')):
            return out_data
    else:
        if isinstance(out_data, type(u'')):
            return out_data.encode('utf-8')
        elif isinstance(out_data, type(str(''))):
            return out_data
    msg = "Invalid value for out_data neither unicode nor byte string: {}".format(out_data)
    raise ValueError(msg)


def write_channel(net_conn, data):
    # Handle the PY2/PY3 differences to write data out to the device.
    net_conn.write(write_bytes(data))


def read_channel(net_conn):
    # Handle the PY2/PY3 differences to write data out to the device.
    return net_conn.read_very_eager().decode('utf-8', 'ignore')


def telnet_connect(ip_addr):
    # Establish telnet connection.
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed-out")


def login(net_conn, username, password):
    # Login to network device.
    output = net_conn.read_until(b"sername:", TELNET_TIMEOUT).decode('utf-8', 'ignore')
    write_channel(net_conn, username + '\n')
    output += net_conn.read_until(b"ssword:", TELNET_TIMEOUT).decode('utf-8', 'ignore')
    write_channel(net_conn, password + '\n')
    return output


def disable_paging(net_conn, paging_cmd='terminal length 0'):
    # Disable the paging of output (i.e. --More--).
    return send_command(net_conn, paging_cmd)


def send_command(net_conn, cmd):
    # Send a command down the telnet channel and return the response.
    cmd = cmd.rstrip()
    write_channel(net_conn, cmd + '\n')
    time.sleep(1)
    return read_channel(net_conn)


"""
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
"""

ip_addr = input("IP address: ")

ip_addr = ip_addr.strip()
username = 'pyclass'
password = getpass()

net_conn = telnet_connect(ip_addr)
output = login(net_conn, username, password)

time.sleep(1)
read_channel(net_conn)
disable_paging(net_conn)

output = send_command(net_conn, 'show ip int brief')

print('\n')
print(output)
print('\n')

net_conn.close()

# EoF
