import requests
from core.searchPJ import searchPJ
from colorama import init, Fore,  Back,  Style
from core.searchPersonne import searchPersonne

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def searchAdresse():
	print(" Nom: ")
	nom = input(f"{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")
	print(" Prenom: ")
	prenom = input(f"{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")
	print(" Code Postal : exemple: 75000 = 75: ")
	postal = input(f"{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")
	print(" Ville (requis) : ")
	city = input(f"{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")
	print("\n"+wait+f" Recherche sur '{prenom} {nom}'...")

	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    'referrer': 'https://google.com',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	'Accept-Encoding': 'gzip, deflate, br',
    	'Accept-Language': 'en-US,en;q=0.9',
    	'Pragma': 'no-cache'
    }

	url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}+{} &ou={}"
	requete = requests.get(url.format(nom, prenom, city), headers=headers)
	searchPJ(requete)