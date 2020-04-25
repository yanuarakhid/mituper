import os
import paramiko
import time
import socket
from getpass import getpass

host = "10.100.69.4"
username = "admin"
passwd = "qwe321"
port = "22"


def menu_manual():
    menu = "menu"
    while menu == "menu":
        os.system("clear")
        print('''
        ========= SELECT THE CONFIGURATION DO YOU WANT ========
    
        [1] Set IP Address
        [2] Enable Web Proxy
        [3] Check Internet Connection (ping google.com)
        [4] Ping to other Host
        [5] System Resource
        [6] Change Password
        [7] Set Identity Router
        [8] Reset Configuration
        [9] Reboot The Router
        [10] Shutdown The Router
        [11] LogOut and Configure Other Router
        [12] Exit                     
        
        ========================================================
        ''')
        choice = int(input("Mituper >> ")or 99)
        if choice == 1:
            os.system("clear")
            show_interface()
            print('''
        ========================================================    
        By Default We Set

        IP Address  : 10.100.88.1
        Prefix      : /24
        Interface   : ether2
        Comment     : MY LAN NETWORK

        You Can Set To Other IP Address, Prefix, Interface, or Comment
        ======================================================== 
            ''')
            input("Enter to Show Interface/IP Address and Continue")
            time.sleep(1)
            show_interface()
            set_ip_address = input("Set IP Address : ") or "10.100.88.1"
            set_prefix = input("Set Prefix : ") or "24"
            set_interface = input("Input your interface : ") or "ether2"
            set_comment = input("Input your interface : ") or "MY LAN NETWORK"
            set_ip(set_ip_address, set_prefix, set_interface, set_comment)
            menu = input() or "menu"
        elif choice == 2:
            print("fitur belum ada")
        elif choice == 3:
            check_connection()
            menu = input() or "menu"
        elif choice == 4:
            ping = input("Ping To : ")
            pingOther(ping)
            menu = input() or "menu"
        elif choice == 5:
            resource()
            menu = input() or "menu"
        elif choice == 6:
            print("fitur belum ada")
            menu = input() or "menu"
        elif choice == 7:
            get_identity()
            name = input("Set Identity Name : ")
            set_identity(name)
            get_identity()
            menu = input() or "menu"
        elif choice == 8:
            print("fitur belum ada")
            menu = input() or "menu"
        elif choice == 9:
            reboot()
            exit()
        elif choice == 10:
            shutdown()
            exit()
        elif choice == 11:
            login()
        elif choice == 12:
            exit()
        elif choice == 99:
            menu_manual()
        else:
            menu = input("Wrong Choice, Please Choice 1, 2, 3") and "menu"
            menu_manual()


def login():
    os.system('clear')
    print('''
    Login into your Mikrotik Routerboard from SSH
    [Press Enter To Use Default Settings]
    Host    : 192.168.88.1
    Username: admin
    Password: (No Password)
    Port    : 22
    ''')
    global host, username, passwd, port
    host = input(
        "Router Address (Ex:example.com/192.168.88.1) : ") or "10.100.69.4"
    username = input("Username  : ") or "admin"
    passwd = getpass("Password: ") or "qwe321"
    port = input("SSH Port : ") or 22
    try:
        ssh_connect = paramiko.SSHClient()
        ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connect.connect(hostname=host, username=username,
                            password=passwd, port=port, timeout=5)
        print("\u001b[32m Connected successfully. \u001b[37m")
        ssh_connect.close()
        menu_manual()
    except paramiko.SSHException:
        print("\u001b[31m Incorrect password \u001b[37m")
        exit()
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("\u001b[31m Unable Connect to Host \u001b[37m")
        exit()
    except socket.timeout:
        print("\u001b[31m Unable to Connect \u001b[37m")
        exit()


def check_connection():
    global host, username, passwd, port
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command('ping count=3 google.com')
    time.sleep(1)

    output = stdout.readlines()
    print("\n".join(output))
    ssh_connect.close()


def pingOther(other):
    global host, username, passwd, port
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command('ping count=5 '+other)
    time.sleep(1)

    output = stdout.readlines()
    print("\n".join(output))
    ssh_connect.close()


def shutdown():
    global host, username, passwd, port
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command('system shutdown;')
    time.sleep(1)


def reboot():
    global host, username, passwd, port
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command('system reboot;')
    time.sleep(1)


def resource():
    global host, username, passwd, port
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command('system resource print')
    time.sleep(1)

    output = stdout.readlines()
    print("\n".join(output))
    ssh_connect.close()


def show_interface():
    global host, username, passwd, port
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command('interface print')
    time.sleep(1)

    output = stdout.readlines()
    print("\n".join(output))
    ssh_connect.close()


def set_ip(ip, prefix, interface, comment):
    global host, username, passwd, port
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command(
        'ip address add address='+ip+'/'+prefix+' interface='+interface+' comment="'+comment+'"')
    time.sleep(1)

    output = stdout.readlines()
    print("\n".join(output))
    ssh_connect.close()
    show_interface()


def get_identity():
    global host, username, passwd, port
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command('system identity print')
    time.sleep(1)

    output = stdout.readlines()
    print("\n".join(output))
    ssh_connect.close()


def set_identity(name):
    global host, username, passwd, port
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=host, username=username,
                        password=passwd, port=port, timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command(
        'system identity set name='+name)
    time.sleep(1)

    output = stdout.readlines()
    print("\n".join(output))
    ssh_connect.close()
