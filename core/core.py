import os
import paramiko
import time
import socket
from selectmenu import SelectMenu
from getpass import getpass

host = "10.100.1.1"
username = "admin"
passwd = ""
port = "22"


def go():
    back = "menu"
    while back == "menu":
        os.system("clear")
        print('''
        ========= SELECT THE CONFIGURATION MODE DO YOU WANT ========

            [1] Manual Configuration
            [2] Automaticaly Configuration Using YAML (One Router)
            [3] Automaticaly Configuration Using YAML (2 or More Router )
            [4] Exit
            
        =============================================================
        ''')
        select = int(input("Mituper >> ")or 5)
        if select == 1:
            menu_manual()
        elif select == 2:
            exit()
        elif select == 3:
            exit()
        elif select == 4:
            exit()
        elif select == 5:
            go()
        else:
            back = input("Wrong Choice, Please Choice 1, 2, 3") and "menu"
            go()


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
        [11] Back
        [12] Exit                     
        
        ========================================================
        ''')
        choice = int(input("Mituper >> ")or 99)
        if choice == 1:
            os.system("clear")
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
            print("fitur belum ada")
            menu = input() or "menu"
        elif choice == 8:
            print("fitur belum ada")
            menu = input() or "menu"
        elif choice == 9:
            print("fitur belum ada")
            menu = input() or "menu"
        elif choice == 10:
            shutdown()
            exit()
        elif choice == 11:
            go()
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
        menu_manual()
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
