import os
import ctypes
import time
import requests
import random
import string
from pystyle import  *


###$$$$$ window settings $$$$$
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def settings():
        ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator | 2loop#6969")
        os.system('mode con: cols=150 lines=30')



discord = 'https://discord.gg/XnRjFmgPYz'



def nitrogenerator(): ###$$$$$ layout $$$$$
    def gentitle():
        settings()
        print("")
        print("")
        print(Colorate.Vertical(Colors.blue_to_cyan, """                                   ╔════════════════════════════════════════════════════════════════════════╗
                                   ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
                                   ║░███╗░░░██╗██╗████████╗██████╗░░██████╗░░░░░░██████╗░███████╗███╗░░░██╗░║
                                   ║░████╗░░██║██║╚══██╔══╝██╔══██╗██╔═══██╗░░░░██╔════╝░██╔════╝████╗░░██║░║
                                   ║░██╔██╗░██║██║░░░██║░░░██████╔╝██║░░░██║░░░░██║░░███╗█████╗░░██╔██╗░██║░║
                                   ║░██║╚██╗██║██║░░░██║░░░██╔══██╗██║░░░██║░░░░██║░░░██║██╔══╝░░██║╚██╗██║░║
                                   ║░██║░╚████║██║░░░██║░░░██║░░██║╚██████╔╝░░░░╚██████╔╝███████╗██║░╚████║░║
                                   ║░╚═╝░░╚═══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░░░░░╚═════╝░╚══════╝╚═╝░░╚═══╝░║
                                   ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
                                   ╚════════════════════════════════════════════════════════════════════════╝""", 2))
        print("")
    def layoutgen():
        cls()
        gentitle()
        print("")
        print(Colorate.Horizontal(Colors.blue_to_purple, f'                                           An easy&&slow :( nitrogen | ' + discord, 2))
        print("")
    def inhowmany(): ###$$$$$ generator $$$$$
        layoutgen()
        while True:
            try:
                howmany = int(input(Colorate.Horizontal(Colors.blue_to_cyan, '                                                                   [howmany@nitro] > ', 2)))
                return howmany
            except ValueError:
                maingenerator()
    def maingenerator():
        results = []
        howmany = inhowmany()
        print("")
        print("")
        print(Colorate.Horizontal(Colors.red_to_yellow, '                                                                   [/] Generating', 2))
        with open('nitrocodes.txt', 'w', encoding='utf-8') as file:
            for i in range(howmany):
                codestring = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
                file.write(f"https://discord.gift/{codestring}\n")
        with open("nitrocodes.txt") as file:
            for codestring in file.readlines():
                nitro = codestring.strip("\n")
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
                nx = requests.get(url)
                if nx.status_code == 200:
                    results.append(f"[+] Valid | {nitro}")
                else:
                    results.append(f"[-] Invalid | {nitro}")
        with open('nitrocodes.txt', 'w') as file:
            file.write('\n'.join(results))
        layoutgen()
        print(Colorate.Horizontal(Colors.green_to_white, '                                                                     Done! ', 2))
        time.sleep(2)
        nitrogenerator()
    maingenerator()


if __name__ == '__main__':
    nitrogenerator()