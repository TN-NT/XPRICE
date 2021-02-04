import requests
from core.searchPJ import searchPJ
from core.searchInfoNumero import searchInfoNumero
from terminaltables import SingleTable
from colorama import init, Fore,  Back,  Style

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def searchPersonne():
	print(" Nom: ")
	nom = input(f"{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")
	print(" Prenom: ")
	prenom = input(f"{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")
	print(" Code Postal : exemple: 75000 = 75: ")
	postal = input(f"{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")
	print(" Ville (requis) : ")
	city = input(f"{Fore.RESET}/{Fore.RED}~{Fore.RESET}> ")
	print("\n"+wait+f" Recherche sur '{prenom} {nom}'...")

	try:

		headers = {
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    	    'referrer': 'https://google.com',
        	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        	'Accept-Encoding': 'utf-8',
        	'Accept-Language': 'en-US,en;q=0.9',
        	'Pragma': 'no-cache'
        }

		# Recherche FR
		url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}+{} &ou={}"
		requete = requests.get(url.format(nom, prenom, city), headers=headers)
		searchPJ(requete)
		# Recherche BE
		url = "https://www.pagesblanches.be/chercher/personne/{}/{}/"
		requete = requests.get(url.format(nom, prenom, city), headers=headers)
		searchPageDor(requete)
		# Recherche CH
		url = "https://tel.local.ch/fr/q?area={}&city=&company=&ext=1&name={}&phone=&rid=455h&street=&typeref=res"
		searchLocalCH(url.format(city, nom, prenom))
		# Recherche LU
		url = "https://www.yellow.lu/fr/pages-blanches/recherche?query={}{}"
		searchYellowLU(url.format(nom, prenom))

		# Copain d'avant search
		searchCopainsdavant(nom, city)

		# url = "https://annuaire.118712.fr/?s={}+{}"
		# Scraping(url.format(prenom, nom))

		# Facebook search		
		fbtool = facebookSearchTool()
		accountsFb = fbtool.searchFacebook(nom, prenom)

		title = " Facebook "

		TABLE_DATA = [
			('Name', 'User', 'Location'),
		]

		count = 0

		for a in accountsFb:
			count += 1
			name = a[1]
			username = a[0]
			fbtool.getInfoProfile(username)
			loc = fbtool.address
			if not loc:
				loc = ""

			tuples = (name, username, loc)
			# listeInfos.append(tuples)
			TABLE_DATA.append(tuples)
		
		if count > 0:
			table_instance = SingleTable(TABLE_DATA, title)
			print(table_instance.table)
		
		# Twitter Search		
		title = " Twitter "

		TABLE_DATA = [
			('Name', 'User', 'Date', 'Location'),
		]

		twitool = twitterSearchTool()
		accountTwitter = twitool.searchTwitter(nom, prenom)

		count = 0

		for a in accountTwitter:
			count += 1
			name = a[1]
			username = "@"+a[0]
			twitool.getInfoProfile(a[0])
			
			location = twitool.location
			date = twitool.birth
			bio = twitool.description
			url = twitool.url

			tuples = (name, username, date, location)
			TABLE_DATA.append(tuples)

		if count > 0:
			table_instance = SingleTable(TABLE_DATA, title)
			print(table_instance.table)
		# Instagram search

		title = " Instagram "

		nom2 = nom + " " + prenom

		instatls = instagramSearchTool()
		instatls.searchInsta(nom2)

		accounts = instatls.accounts

		TABLE_DATA = [
			('Name', 'User'),
		]

		count = 0

		for account in accounts:
			url = "https://instagram.com/"+account
			i = instagramSearchTool()
			i.getInfo(url)
			name = i.name

			tuples = (name, account)
			TABLE_DATA.append(tuples)

			count +=1

		if count > 0:
			table = SingleTable(TABLE_DATA, title)
			print(table.table)


		profiler(nom, prenom)

	except IOError:
		pass
