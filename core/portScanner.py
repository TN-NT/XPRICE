import socket
import _thread
import time
from colorama import Fore, init
import os

def portscan():
    ip = input(f"Enter ip to scan:\n{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")
    os.system("curl http://api.hackertarget.com/nmap/?q=" + ip )