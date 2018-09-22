'''
This script is based on my home equipment as opposed to the Class Lab so I could use 
the Spectrum email account.

Using SNMPv3 create a script that detects router configuration changes.

If the running configuration has changed, then send an email notification to yourself identifying the router that changed and the time that it changed.

Note, the running configuration of pynet-rtr2 is changing every 15 minutes (roughly at 0, 15, 30, and 45 minutes after the hour). This will allow you to test your script in the lab environment. 

Cisco routers have the following three OIDs:

# Uptime when running config last changed
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'   

# Uptime when running config last saved
# note any 'write' constitutes a save    
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'   

# Uptime when startup config last saved   
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'


From the above descriptions, the router will save the sysUptime timestamp (OID sysUptime = 1.3.6.1.2.1.1.3.0) when a running configuration change occurs. The router will also record the sysUptime timestamp when the running configuration is saved to the startup config. Note, sysUptime times are in hundredths of seconds
'''

import snmp_helper
import email_helper
import yaml

# SNMP Information for the Switch
ip_addr = '10.0.0.1'
a_user = 'SNMPv3user'
auth_key = 'MyAuthen'
encrypt_key = 'MyEncrypt'
snmp_user = (a_user, auth_key, encrypt_key)
John_Michael = (ip_addr, 161)

# Obtain and save intitial control data
sysname = snmp_helper.snmp_get_oid_v3(John_Michael, snmp_user, oid=  '1.3.6.1.2.1.1.5.0')
sysname = snmp_helper.snmp_extract(sysname)
last_known_modify = snmp_helper.snmp_get_oid_v3(John_Michael, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.1.0')
last_known_modify = snmp_helper.snmp_extract(last_known_modify)
last_known_write = snmp_helper.snmp_get_oid_v3(John_Michael, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.2.0')
last_known_write = snmp_helper.snmp_extract(last_known_write)

my_dict = {
    'sysname': sysname,
    'last_known_modify': last_known_modify,
    'last_known_write': last_known_write,
}

filename = r'C:/Users/Jon/PyNet_Class/running-config_change.yml'
with open(filename, 'w') as file:
    output=yaml.dump(my_dict, file, default_flow_style=False)


uptime = snmp_helper.snmp_get_oid_v3(John_Michael, snmp_user, oid='1.3.6.1.2.1.1.3.0')
uptime = snmp_helper.snmp_extract(uptime)
last_modify = snmp_helper.snmp_get_oid_v3(John_Michael, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.1.0')
last_modify = snmp_helper.snmp_extract(last_modify)
last_write = snmp_helper.snmp_get_oid_v3(John_Michael, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.2.0')
last_write = snmp_helper.snmp_extract(last_write)

with open(filename) as file:
    input = yaml.load(file)

if input['last_known_modify'] == last_modify:
    print()
    print('No configuration changes.')
    print()
else:
    print()
    print('A configuration change on', my_dict['sysname'],'has been detected.')
    change_was = (int(last_modify) - int(input['last_known_modify'])) / 100
    print('The change was', change_was, 'seconds after the last change.')
    
    # Send an email alert
    recipient = 'b17gunnr@nycap.rr.com'
    subject = 'Test Message'
    message = 'A configuration change has been detected'
    sender = 'b17gunnr@nycap.rr.com'
    email_helper.send_mail(recipient, subject, message, sender)
    
    # Update the timers
    my_dict['last_known_modify'] = last_modify
    
    filename = r'C:/Users/Jon/PyNet_Class/running-config_change.yml'
    with open(filename, 'w') as file:
        output=yaml.dump(my_dict, file, default_flow_style=False)

