# Random_Mac_Changer_Linux
This program is a Python script that allows you to change the MAC address of your Linux computer's network interface to a randomly generated value.

# Usage

1. Open a terminal on your Linux computer.

2. Clone the repository or download the change_mac_address.py file.

3. Navigate to the directory containing the change_mac_address.py file.

4. Run the script using the following command: python3 change_mac_address.py.

5. Enter the name of the network interface that you want to change the MAC address for. You can find the name of your network interface by running the ifconfig command in the terminal.

6. The script will generate a new MAC address and apply it to the specified network interface. If the operation is successful, you will see a success message in the terminal. If there is an error, you will see an error message instead.

# Example

$ python3 change_mac_address.py

Enter interface name: eth0

Successfully changed MAC address of eth0 to 00:16:3e:12:34:56

# Note
Depending on your Linux distribution and configuration, you may need to run the script as root (using sudo) to have sufficient permissions to change the MAC address.
