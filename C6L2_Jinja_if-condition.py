#!/usr/bin/env python

'''
Expand upon exercise 1 to generate the following: 

--------
interface Loopback0
 ip address 172.31.255.1 255.255.255.255

router ospf 40
 network 10.220.88.0 0.0.0.255 area 0
--------

The Jinja2 template should be read from an external file named 'ospf_config.j2'.

The following items should all be variables in the template: process_id, network, wildcard, area, loopback0_addr, loopback0_mask.

Additionally, the 'interface Loopback0' and its ip address configuration should only be generated if the loopback0_addr variable is defined (i.e. use an if-condition here).

'''

from __future__ import print_function, unicode_literals, division
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

script_vars = {
    'process_id': 40,
    'network': '10.220.88.0',
    'wildcard': '0.0.0.255', 
    'area': 0,
    'ip_addr': '172.31.255.1',
    'netmask': '255.255.255.255',
}

template_file = 'C6L2_ospf_config.j2'
template = env.get_template(template_file)
output = template.render(**script_vars)

print(output)

# EoF
