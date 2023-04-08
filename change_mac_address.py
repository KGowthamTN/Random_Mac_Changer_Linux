#!/usr/bin/env python3
import subprocess
import random

def get_mac(interface):
    # run the command to get the current MAC address
    output = subprocess.check_output(['ifconfig', interface])
    mac = output.split()[4].decode()

    return mac

def change_mac(interface):
    # generate a random MAC address
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), 
           random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    mac_str = ':'.join(map(lambda x: "%02x" % x, mac))

    # run the command to change the MAC address
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac_str])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])

    new_mac = get_mac(interface)
    if new_mac == mac_str:
        print(f'Successfully changed MAC address of {interface} to {mac_str}')
    else:
        print('Error: Failed to change MAC address')

if __name__ == '__main__':
    interface = input('Enter interface name: ')
    change_mac(interface)
