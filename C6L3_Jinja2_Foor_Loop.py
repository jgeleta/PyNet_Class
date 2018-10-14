#!/usr/bin/env python

'''
Expand upon exercise2 to generate the following: 

--------
interface Loopback0
 ip address 172.31.255.1 255.255.255.255

router ospf 40
 network 10.220.88.0 0.0.0.255 area 0
 network 172.31.255.28 0.0.0.0 area 1
--------

The Jinja2 template should be read from an external file named 'ospf_config_for.j2'.

The OSPF 'network' statements should be generated using a for-loop embedded in the Jinja2 template.

You should have a Python data structure named 'ospf_networks' that you iterate over (in your Jinja2 for-loop). At the highest-level this data structure should be either a list or a dictionary.

The following items should all be variables in the template:
process_id
network*
wildcard*
area*
loopback0_addr
loopback0_maks

* Contained inside of the ospf_networks variable

Additionally, the interface Loopback0 and its ip address config should only be generated if the loopback0_addr variable is defined (i.e. use an if-condition here).

'''

from __future__ import print_function, unicode_literals, division
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

networks = [
    {'network': '10.220.88.0', 'wildcard': '0.0.0.255', 'area': 0},
    {'network': '172.31.255.28', 'wildcard': '0.0.0.0', 'area': 1},
]

script_vars = {
    'process_id': 40,
    'network': networks,
    'ip_addr': '172.31.255.1',
    'netmask': '255.255.255.255',
}

template_file = 'C6L3_ospf_config_for.j2'
template = env.get_template(template_file)
output = template.render(**script_vars)

print(output)

# EoF
