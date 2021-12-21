import socket
import subprocess

def main():
    print("\nScanning the network...\n")
    hostname = socket.gethostname()
    ip_address = "192.168.1.1"
    print("Hostname: " + hostname)
    print("IP Address: " + ip_address + "\n")
    split_ip = ip_address.split(".")

    clients = []

    for i in range(1, 254):
        address = split_ip[0] + "." + split_ip[1] + "." + split_ip[2] + "." + str(i)

        request = subprocess.call(['ping', '-c', '1', address, '-v', '0', '-W', '3'])

        if request == 0:
            clients.append(address)

    print("\nList of available clients :\n")

    for client in clients:
        print("IP Address: " + client)

if __name__ == "__main__":
    main()
