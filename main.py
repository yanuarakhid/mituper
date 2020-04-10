#!/usr/bin/python
from manual import manual
from multirouter import multirouter
from singlerouter import singlerouter
import os
import time


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
            manual.login()
        elif select == 2:
            singlerouter.go()
        elif select == 3:
            exit()
        elif select == 4:
            exit()
        elif select == 5:
            go()
        else:
            back = input("Wrong Choice, Please Choice 1, 2, 3") and "menu"
            go()


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
    go()


if __name__ == "__main__":
    main()
