import socket
import subprocess
import time
from tqdm import tqdm


def main():

    # Getting the host name
    hostname = socket.gethostname()

    # It's out basic IP Address inside the LAN
    ip_address = "192.168.1.1"
    print("\nHostname: " + hostname)
    print("IP Address: " + ip_address)

    print("\nScanning the network...\n")

    # Split so we can modify each values
    split_ip = ip_address.split(".")

    # Output array
    clients = []

    # How many addresses we want to scan
    length = 255

    start = time.time()

    # Using tqdm to create progress bar
    for i in tqdm(range(length), desc="Analysing..."):

        # Recreate the ip address, changing the end
        address = split_ip[0] + "." + split_ip[1] + "." + split_ip[2] + "." + str(i)

        # Executing the ping command, it's slow but launching an ARP request as well
        subprocess.call(['ping', '-c 1', '-i 0,2', '-W 0,1', address], stdout=subprocess.DEVNULL)

    # Reading ARP table
    arp = subprocess.Popen(['arp', '-a'], stdout=subprocess.PIPE)

    # Keeping correct addresses
    for line in arp.stdout:
        line = line.decode('utf-8')
        if '?' not in line and line not in clients:
            clients.append(line)

    end = time.time()

    print("\nList of available clients :\n")

    for client in clients:
        print(client)

    print(f"\nTime elapsed {end - start} seconds")


if __name__ == "__main__":
    main()
