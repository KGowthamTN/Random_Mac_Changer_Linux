import subprocess
import random

def get_random_mac():
    # Generate a random MAC address
    mac = [ 0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff) ]
    return mac

def change_mac_address(interface):
    # Generate a new MAC address
    new_mac = ':'.join(map(lambda x: "%02x" % x, get_random_mac()))

    # Turn off the interface
    subprocess.call(['ifconfig', interface, 'down'])

    # Set the new MAC address
    subprocess.call(['ip', 'link', 'set', 'dev', interface, 'address', new_mac])

    # Turn on the interface
    subprocess.call(['ifconfig', interface, 'up'])

    # Check if the MAC address has been changed
    p = subprocess.Popen(['ip', 'link', 'show', interface], stdout=subprocess.PIPE)
    output = p.communicate()[0]
    if new_mac.lower() in output.decode().lower():
        print(f"Successfully changed MAC address of {interface} to {new_mac}")
    else:
        print(f"Error: Failed to change MAC address of {interface}")

if __name__ == '__main__':
    # Get the name of the network interface from the user
    interface = input("Enter interface name: ")

    # Change the MAC address of the specified interface
    change_mac_address(interface)
