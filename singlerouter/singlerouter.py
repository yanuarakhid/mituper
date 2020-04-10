import os
import yaml
import paramiko
import time
import socket
from getpass import getpass


fileDir = os.path.dirname(os.path.realpath('__file__'))
config_yaml = os.path.join(fileDir, 'mituper/singlerouter.yaml')
with open(config_yaml, 'r') as cfg:
    config = yaml.safe_load(cfg)


def go():
    global config
    os.system("clear")
    print('''
        =====================================================
                AUTOMATIC CONFIGURATION USING YAML
        =====================================================
        ''')
    print("Testing Connetion to Router....")
    os.system("ping -c 5 "+config["ip"])
    time.sleep(1)
    print(
        "\nTrying SSH Login into Router (\u001b[32m"+config["ip"]+"\u001b[37m) Port : \u001b[32m"+config["ssh_port"]+"\u001b[37m ....")
    try:
        ssh_connect = paramiko.SSHClient()
        ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connect.connect(hostname=config["ip"], username=config["username"],
                            password=config["password"], port=config["ssh_port"], timeout=5)
        print("\u001b[32m Connected successfully. \u001b[37m")
        ssh_connect.close()
        time.sleep(1)
        os.system("clear")
        print("Configuring IP Address...........")
        time.sleep(2)
        for con_ip in config["interface"]:
            set_ip(con_ip["ip_address"], con_ip["int"], con_ip["comment"])
        print("Mantap")
    except paramiko.SSHException:
        print("\u001b[31m Incorrect password \u001b[37m")
        exit()
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("\u001b[31m Unable Connect to Host \u001b[37m")
        exit()
    except socket.timeout:
        print("\u001b[31m Unable to Connect \u001b[37m")
        exit()
    exit()


def set_ip(ip, interface, comment):
    global config
    ssh_connect = paramiko.SSHClient()
    ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connect.connect(hostname=config["ip"], username=config["username"],
                        password=config["password"], port=config["ssh_port"], timeout=5)
    stdin, stdout, stderr = ssh_connect.exec_command(
        'ip address add address='+ip+' interface='+interface+' comment="'+comment+'"')
    time.sleep(1)
    ssh_connect.close()
