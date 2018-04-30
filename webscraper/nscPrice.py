import requests
import webbrowser
from bs4 import BeautifulSoup

url ="http://www.moneycontrol.com/india/stockpricequote/banks-private-sector/idfcbank/IDF01"
site = requests.get(url)
#print(site.text)
soup = BeautifulSoup(site.text,"html.parser")
for link in soup.select('#Nsc_Prc_tick_div'):
    print(link)
    name = link.get('strong')
    print(name)
