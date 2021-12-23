import time

from scapy.layers.l2 import ARP, Ether
import socket
from scapy.all import srp


def main():

    # Getting the host name
    hostname = socket.gethostname()

    # It's out basic IP Address inside the LAN
    ip_address = "192.168.1.1/24"
    print("\nHostname: " + hostname)
    print("IP Address: " + ip_address)

    print("\nScanning the network...\n")

    # ARP packet
    arp = ARP(pdst=ip_address)

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp

    result = srp(packet, timeout=3)[0]

    clients = []

    for sent, received in result:
        clients.append("IP : " + received.psrc + " | MAC : " + received.hwsrc)

    for client in clients:
        print(client)


if __name__ == "__main__":
    main()
