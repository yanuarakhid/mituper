#!/usr/bin/python
# from interface import interface
import os
import paramiko
import time
from getpass import getpass

os.system('clear')
print(
    '''\u001b[31m
███╗   ███╗    ███████╗    ██╗  ██╗
████╗ ████║    ██╔════╝    ██║  ██║
██╔████╔██║    ███████╗    ███████║
██║╚██╔╝██║    ╚════██║    ██╔══██║
██║ ╚═╝ ██║    ███████║    ██║  ██║
╚═╝     ╚═╝    ╚══════╝    ╚═╝  ╚═╝ 

    "MIKROTIK-SETUP-HELPER"
\u001b[37m
Created By  : Akhid Yanuar A.F
Follow me   : @yanuarakhid
Version     : 0.1
Desc        : "Mikrotik Helper Configuration Using SSH"
'''
)


input("Press Enter To Begin")
time.sleep(2)
os.system('clear')

print("Login into your Routerboard from SSH")

host = input("Router Address (Ex:example.com/10.100.1.1) : ")
username = input("Username  : ")
passwd = getpass("Password: ")
choice = input("Are You Using Default SSH Port (22) ? (Y/n) : ")
if choice == 'y':
    port = 22
elif choice == 'n' or choice == 'N':
    port = input("Your Custom SSH Port : ")
else:
    port = 22


print(port)
try:
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    print("Connected successfully.")
except paramiko.SSHException:
    print("Incorrect password")

stdin, stdout, stderr = ssh_connect.exec_command('ip route print')
time.sleep(1)

output = stdout.readlines()
print("\n".join(output))
ssh_connect.close()
time.sleep(500)


print(
    '''
    1. Configure IP Address (Static)
    2. Configure IP Address From DHCP Client
    3. Configure IP Route
    4. Configure NAT for Internet
    5. Configure DNS Server
    6. Configure DHCP Server
    '''
)
