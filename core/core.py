import os
from selectmenu import SelectMenu
import paramiko
import time
import socket
from getpass import getpass


def go():
    os.system("clear")
    menu = SelectMenu()
    menu.add_choices(["Manual Configuration", "Automaticaly Configuration Using YAML (One Router)",
                      "Automaticaly Configuration Using YAML (2 or More Router )", "Exit"])
    result = menu.select(
        "========= SELECT THE CONFIGURATION DO YOU WANT ========")
    if result == "Manual Configuration":
        menu_manual()
    elif result == "Automaticaly Configuration Using YAML (One Router)":
        exit()
    elif result == "Automaticaly Configuration Using YAML (2 or More Router )":
        exit()
    elif result == "Exit":
        exit()


def menu_manual():
    menu = "menu"
    while menu == "menu":
        os.system("clear")
        print(
            '''
            ------------ CONFIGURATION MENU -----------

            [1] Automaticaly Configure Network 
            [2] Set IP Address
            [3] Enable Web Proxy
            [4] Check Internet Connection (ping google.com)
            [5] Ping to other Host
            [6] System Resource
            [7] Change Password
            [8] Set Identity Router
            [9] Reset Configuration
            [10] Reboot The Router
            [11] Shutdown The Router
            [12] Exit Program

            -------------------------------------------
            '''
        )

        choice = input("Input The number Coice : ")
        choice = int(choice)
        if choice == 1:
            os.system("clear")
            automatic()
            menu = input() or "menu"
        elif choice == 2:
            os.system("clear")
            print('''
By Default We Set

IP Address  : 10.100.88.1
Prefix      : /24
Interface   : ether2
Comment     : MY LAN NETWORK

You Can Set To Other IP Address, Prefix, Interface, or Comment
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
        elif choice == 3:
            print("fitur belum ada")
        elif choice == 4:
            check_connection()
            menu = input() or "menu"
        elif choice == 5:
            ping = input("Ping To : ")
            pingOther(ping)
            menu = input() or "menu"
        elif choice == 6:
            resource()
            menu = input() or "menu"
        elif choice == 7:
            print("fitur belum ada")
            menu = input() or "menu"
        elif choice == 8:
            print("fitur belum ada")
            menu = input() or "menu"
        elif choice == 9:
            print("fitur belum ada")
            menu = input() or "menu"
        elif choice == 10:
            print("fitur belum ada")
            menu = input() or "menu"
        elif choice == 11:
            shutdown()
            exit()
        elif choice == 12:
            exit()
        else:
            print("Wrong Choice, Please Choice 1, 2, 3")
            menu = input() or "menu"


host = "10.100.1.1"
username = "admin"
passwd = ""
port = "22"


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
        "Router Address (Ex:example.com/192.168.88.1) : ") or "10.100.69.17"
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
        menu()
    except paramiko.SSHException:
        print("\u001b[31m Incorrect password \u001b[37m")
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("\u001b[31m Unable Connect to Host \u001b[37m")
    except socket.timeout:
        print("\u001b[31m Unable to Connect \u001b[37m")


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


def automatic():
    print('''
By Default We Set

1. DHCP Client For Your WAN in ether1
  (Please Plug Your Source Internet (WAN) in ether 1
2. And For Your LAN Address 
    IP Address  : 10.100.88.1
    Prefix      : /24
    Interface   : ether2
    Comment     : MY LAN NETWORK
3. Set DHCP Server for Your LAN Network
4. And Include Set The NAT (Network Address)

Dont Worry You Can Also set Manualy :)
            ''')
    ether_wan = input(
        "Where You Plug Internet Cable (as Your WAN) ex. ether1 : ")
    dhcp_or_static = input("Set Your WAN with DHCP Client or Static ? Y/n")
    if dhcp_or_static == 'Y' or 'y':
        print("hehehe")
    elif dhcp_or_static == 'N' or 'n':
        print("hiya")
    else:
        print("hiya salah")
    ether_lan = input("Input Your Ether for LAN ex.ether2 : ")
    lan = input("Input Your LAN Network Address ex.10.100.1.1 : ")
    prefix = input("Input your lan Address Prefix ex. 24 : ")
