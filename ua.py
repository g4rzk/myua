import os
import requests
from bs4 import BeautifulSoup as parser

class Main:
	def __init__(self):
		url_main = "https://www.whatsmyua.info"
		self.banner() 
		print(f" +--------------------------------------------------")
		uas = input(" | Your User-Agent : ")
		
		#// find info from user agent
		s = parser(requests.get(url_main, headers={"user-agent":uas}).text, "html.parser")
		raw_ua = s.find("li", id="rawUa").text
		family = s.find("li", id="family").text
		name_hp = s.find("li", id="product").text
		os_ = s.find("li", id="os").text
		ly = s.find("li", id="layout").text
		
		self.p_main(url_main, raw_ua, family, name_hp, os_, ly)
	
	def banner(self):
		os.system("clear")
		print(f"       __  __      _   _  _   \n      |  \/  |_  _| | | |/_\  \n      | |\/| | || | |_| / _ \ \n      |_|  |_|\_, |\___/_/ \_\ \n              |__/ ^whatsmyua.info")
		
	def p_main(self, url_main, raw_ua, family, name_hp, os_, ly):
		ua = raw_ua.replace("rawUa: ", "")
		browser = family.replace("family: ", "")
		hp = name_hp.replace("product: ", "")
		os = os_.replace("os: ", "")
		layout = ly.replace("layout: ", "")
		
		print(f" +--------------------------------------------------")
		print(f" | INFO YOUR USER AGENT : ")
		print(f" |")
		print(f" | OS      : {os}")
		print(f" | Layout  : {layout}")
		print(f" | Product : {hp}")
		print(f" | Browser : {browser}")
		print(f" +--------------------------------------------------")
		print(f" | Website : {url_main}")
		exit(f" +--------------------------------------------------")
		


Main()