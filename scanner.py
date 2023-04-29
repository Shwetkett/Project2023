import pyfiglet
import socket
from IPy import IP

ascii_banner = pyfiglet.figlet_format("PORT SCANNER   Aman & Shwetket  ")
print(ascii_banner)

def scan(target, port_num):
    ports = []
    converted_ip = check_ip(target)
    print('\n' + '[Scanning Target...] ' + str(target))
    for port in range(1, port_num):
        result = scan_port(converted_ip, port)
        if result != None:
            ports.append(result)
    return ports

def get_banner(s):
    return s.recv(1024)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.1)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            return(str(port) + ' : ' + str(banner.decode().strip('\n').strip('\r')))
        except:
            return(str(port))
    except:
        pass


if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan (split multiple targets with ,): ')
    port_number = int(input('[+] Enter Number Of Ports You Want To Scan: '))
    if ',' in targets:
        for ip_add in targets.split(','):
            print(scan(ip_add.strip(' '), port_number))
    else:
        print(scan(targets, port_number))
