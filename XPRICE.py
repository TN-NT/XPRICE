import os
import time
import colorama
import webbrowser
import requests
import sys, random, time, importlib
from terminaltables import SingleTable
from colorama import *
from requests import get
import os
import ctypes
import csv
import getpass
import sys
from datetime import date
import terminal_banner
from colorama import Fore, Back, Style, init
colorama.init()
#from Base
from core.google import google
from core.ipfinder import ipFinder
from core.searchAdresse import searchAdresse
#from end
ctypes.windll.kernel32.SetConsoleTitleW('[ #XPRICE TOOLS BY TIAGZ]') 
os.system('cls')
print(Fore.RED + 'Checking for',Fore.WHITE + 'new updates...')
version = "https://pastebin.com/raw/TQx3gktP"
actuel_version = 1.0
r = requests.get(version)
texte = r.text

banner_tiagzs = """

  ██╗ ██╗ ██╗  ██╗██████╗ ██████╗ ██╗ ██████╗███████╗
 ████████╗╚██╗██╔╝██╔══██╗██╔══██╗██║██╔════╝██╔════╝
 ╚██╔═██╔╝ ╚███╔╝ ██████╔╝██████╔╝██║██║     █████╗  
 ████████╗ ██╔██╗ ██╔═══╝ ██╔══██╗██║██║     ██╔══╝  
 ╚██╔═██╔╝██╔╝ ██╗██║     ██║  ██║██║╚██████╗███████╗
 ╚═╝ ╚═╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝

      [1] IP-Finder                   [06] Email lookup               
      [2] Google-Search-Anonyme       [07] Twitter info             ╔═════════════════════════╗
      [3] Leaked-Price                [08] Instagram info           ║ ./ Créer par : TIAGZ    ║     
      [4] Lookup ++                   [09] Github scraper           ║ ./ Version   : 1.0      ║
      [5] Profiler                    [10] Username Scraper         ║ ./ Langue    : FR       ║
                                                                    ╚═════════════════════════╝
 
      [b] back main menu    [e] Exit script    [c] Clear Screen
"""

if texte != str(actuel_version):
    print(Fore.RED + "Nouvelle mise à jour" ,Fore.WHITE + "disponnible merci de la télécharger")
    print(Fore.RED + 'Fermeture' ,Fore.WHITE + 'dans 5 seconds')
    time.sleep(5)
    webbrowser.open('https://discord.gg/EYVyCqb4Qg')
    exit()

time.sleep(1) 

print("")
print(Fore.RED + "Update",Fore.WHITE + " : Vous êtes à jour") 
print(Fore.RED + "Message",Fore.WHITE + ": Pense au salon vouches si tu n'a pas déjà posté ton avis sur XPRICE")

print("")
print("")
print("")
print("")
print("")
print(Fore.RED + "   ██╗ ██╗ ",Fore.WHITE + "██╗  ██╗██████╗ ██████╗ ██╗ ██████╗███████╗") 
print(Fore.RED + "  ████████╗",Fore.WHITE + "╚██╗██╔╝██╔══██╗██╔══██╗██║██╔════╝██╔════╝")
print(Fore.RED + "  ╚██╔═██╔╝",Fore.WHITE + " ╚███╔╝ ██████╔╝██████╔╝██║██║     █████╗  ")
print(Fore.RED + "  ████████╗",Fore.WHITE + " ██╔██╗ ██╔═══╝ ██╔══██╗██║██║     ██╔══╝  ")
print(Fore.RED + "  ╚██╔═██╔╝",Fore.WHITE + "██╔╝ ██╗██║     ██║  ██║██║╚██████╗███████╗")
print(Fore.RED + "   ╚═╝ ╚═╝ ",Fore.WHITE + "╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝")

banner_tiagz = Fore.YELLOW + """
      [1] IP-Finder                   [06] Email lookup               
      [2] Google-Search-Anonyme       [07] Twitter info             ╔═════════════════════════╗
      [3] Leaked-Price                [08] Instagram info           ║ ./ Créer par : TIAGZ    ║     
      [4] Lookup ++                   [09] Github scraper           ║ ./ Version   : 1.0      ║
      [5] Profiler                    [10] Username Scraper         ║ ./ Langue    : FR       ║
                                                                    ╚═════════════════════════╝
 
      [b] back main menu    [e] Exit script    [c] Clear Screen
"""
print(banner_tiagz)

loop=True    
while loop:
 while True:
        choix = input(f"{Fore.RED}user@xprice {Fore.GREEN}►{Fore.CYAN} /xprice {Fore.RED}# ")

        if choix == "1":
            ipFinder()

        if choix == "2":
            google()  

        if choix == "3":
            githubscraper()  

        if choix == "4":
            searchAdresse()
                  

        if choix == "b":
            os.system('cls')
            print(banner_tiagzs)

        if choix == "e":
            exit()   

        if choix == "c":
            os.system('cls')
            print(banner_tiagzs) 
        else:
            pass
