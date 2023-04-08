import subprocess
import random
import re

def get_interface_name():
    # prompt user to enter interface name
    interface = input("Enter interface name: ")
    return interface

def generate_mac_address():
    # generate random MAC address
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    mac_str = ':'.join(map(lambda x: "%02x" % x, mac))
    return mac_str

def set_mac_address(interface, mac_str):
    # set new MAC address using ifconfig
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac_str])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])

def get_current_mac_address(interface):
    # retrieve current MAC address
    output = subprocess.check_output(['ifconfig', interface]).decode()
    mac_search = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', output)
    if mac_search:
        return mac_search.group(0)
    else:
        return None

def main():
    # get interface name from user
    interface = get_interface_name()

    # generate and set new MAC address
    new_mac = generate_mac_address()
    set_mac_address(interface, new_mac)

    # check if the MAC address was successfully changed
    current_mac = get_current_mac_address(interface)
    if current_mac == new_mac:
        print(f"Successfully changed MAC address of {interface} to {new_mac}")
    else:
        print("Error: Failed to change MAC address")

if __name__ == '__main__':
    main()
