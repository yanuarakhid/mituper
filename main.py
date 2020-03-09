#!/usr/bin/python
import os
import paramiko
import time
from getpass import getpass

os.system('clear')
print(
    '''
██╗     ███████╗██╗  ██╗██████╗ ███████╗██╗  ██╗
██║     ██╔════╝██║ ██╔╝██╔══██╗██╔════╝██║ ██╔╝
██║     █████╗  █████╔╝ ██████╔╝█████╗  █████╔╝
██║     ██╔══╝  ██╔═██╗ ██╔══██╗██╔══╝  ██╔═██╗
███████╗███████╗██║  ██╗██║  ██║███████╗██║  ██╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
Created By  : Akhid Yanuar A.F
Follow me   : @yanuarakhid
Version     : 0.1
"Mikrotik Helper Configuration Using SSH"
'''
)

host = input("Router Address (Ex:example.com/10.100.1.1) : ")
username = input("Username  : ")
passwd = getpass("Password: ")
choice = input("Are You Using Default SSH Port (22) ? (Y/n) : ")
if choice == 'y':
    port = 22
elif choice == 'n':
    port = input("Your Custom SSH Port :")
else:
    port = 22


# ssh_connect = paramiko.SSHClient()
# ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_connect.connect(hostname=host, username=username,
#                     password=passwd, port=port, timeout=5)

# print("Conencting....")
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
