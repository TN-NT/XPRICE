import os
import requests
import time
import colorama
import webbrowser
import urllib.request
from terminaltables import SingleTable
from terminaltables import SingleTable
from colorama import *
from requests import get
import ctypes
import os
import ctypes
from colorama import Fore, Back, Style, init
colorama.init()

ctypes.windll.kernel32.SetConsoleTitleW('[BY </> TIAGZ#0001 XPRICE IP LOOKUP 1.0')


banner = """
  ___ ____    _                _                
 |_ _|  _ \  | |    ___   ___ | | ___   _ _ __  
  | || |_) | | |   / _ \ / _ \| |/ / | | | '_ \ 
  | ||  __/  | |__| (_) | (_) |   <| |_| | |_) |
 |___|_|     |_____\___/ \___/|_|\_\\__,_ | .__/  
                                         |_|    
 DISCORD : </> TIAGZ-UHQ#0001
 Github : https://github.com/tn-nt
"""

def ipFinder():
    os.system('cls')
    print(banner)
    print("Type the IP number to track: ")
    ipinfo = input(f"{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")

    getIpInfo = get(f'http://ip-api.com/json/{ipinfo}?fields=status,continent,continentCode,country,countryCode,region,regionName,city,timezone,isp,query')
    getIpInfoResult = getIpInfo.json()

    table_data = [
    ['IP', 'COUNTRY','STATE', 'CITY','TIMEZONE', 'PROVIDER'],
    [f'{getIpInfoResult["query"]}', f'{getIpInfoResult["country"]} {getIpInfoResult["countryCode"]}', f'{getIpInfoResult["regionName"]}', f'{getIpInfoResult["city"]}', f'{getIpInfoResult["timezone"]}', f'{getIpInfoResult["isp"]}']
    ]
    table = SingleTable(table_data)
    print("\n" + table.table + "\n")
    input()
