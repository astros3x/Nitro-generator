import os
import time
import ctypes
import string
import requests
import threading
from random import *
from pystyle import  *

#SETTINGS
#####################################################################
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def settings():
        ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator | v2.0")
        os.system('mode con: cols=150 lines=30')
#####################################################################



# LAYOUT
#####################################################################
def nitrogenerator(): 
    def gentitle():
        settings()
        print("")
        print("")
        print(Colorate.Vertical(Colors.blue_to_cyan, f"""                                   ╔════════════════════════════════════════════════════════════════════════╗
                                   ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
                                   ║░███╗░░░██╗██╗████████╗██████╗░░██████╗░░░░░░██████╗░███████╗███╗░░░██╗░║
                                   ║░████╗░░██║██║╚══██╔══╝██╔══██╗██╔═══██╗░░░░██╔════╝░██╔════╝████╗░░██║░║
                                   ║░██╔██╗░██║██║░░░██║░░░██████╔╝██║░░░██║░░░░██║░░███╗█████╗░░██╔██╗░██║░║
                                   ║░██║╚██╗██║██║░░░██║░░░██╔══██╗██║░░░██║░░░░██║░░░██║██╔══╝░░██║╚██╗██║░║
                                   ║░██║░╚████║██║░░░██║░░░██║░░██║╚██████╔╝░░░░╚██████╔╝███████╗██║░╚████║░║
                                   ║░╚═╝░░╚═══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░░░░░╚═════╝░╚══════╝╚═╝░░╚═══╝░║
                                   ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
                                   ╚════════════════════════════════════════════════════════════════════════╝

                                   |     .gg/astros3x     |      Nitro Generator     |  by AstriDevelopers  |\n\n\n""", 2))
    def layoutgen():
        cls()
        gentitle()
#####################################################################



#GEN SYSTEM
#####################################################################
    def inhowmany():
        layoutgen()
        while True:
            try:
                howmany = int(input(Colorate.Horizontal(Colors.blue_to_cyan, '                                                                 [howmany@nitro] > ', 2)))
                return howmany
            except ValueError:
                maingenerator()
    global content
    content = ""        
    def nitro():
            global content
            nitro = "".join(choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
            nitro = f"https://discord.gift/{nitro}"
            url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            nx = requests.get(url)
            if nx.status_code == 200:
                content += f"[+] Valid | {nitro}\n"
            else:
                content += f"[-] Invalid | {nitro}\n"
    def maingenerator():
        howmany = inhowmany()
        layoutgen()
        print(Colorate.Horizontal(Colors.blue_to_cyan, '                                                               [generating@nitro] > ', 2))
        threads = []
        for x in range(howmany):
            thread = threading.Thread(target=nitro)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        open("nitrocodes.txt", "w").write(content)
        layoutgen()
        print(Colorate.Horizontal(Colors.green_to_white, '                                                                     Done! ', 2))
        time.sleep(2)
        nitrogenerator()
    maingenerator()
#####################################################################



if __name__ == '__main__':

# OUR DISCORD = discord.gg/astros3x

    nitrogenerator()