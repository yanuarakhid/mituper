#!/usr/bin/python
from core import core
import os
import time


def main():
    os.system('clear')
    print('''\u001b[32m
███╗   ███╗██╗████████╗██╗   ██╗██████╗ ███████╗██████╗ 
████╗ ████║██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║   ██║   ██║   ██║██████╔╝█████╗  ██████╔╝
██║╚██╔╝██║██║   ██║   ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║   ██║   ╚██████╔╝██║     ███████╗██║  ██║
╚═╝     ╚═╝╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                        
                "MIkrotik-seTUp-helPER"
    \u001b[37m
        https://github.com/yanuarakhid/mituper

    Created By  : Akhid Yanuar A.F
    Follow me   : @yanuarakhid
    Version     : 0.1
    Desc        : "Mikrotik Helper Configuration Using SSH"
    
    ''')
    input("Press Enter To Begin")
    time.sleep(1)
    core.go()


if __name__ == "__main__":
    main()
