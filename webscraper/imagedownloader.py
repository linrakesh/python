import urllib.request
import requests
import random
import webbrowser,sys
import os
import tkinter as tk
from bs4 import BeautifulSoup
from tkinter import filedialog

def downloader(image_url,path):
    file_name = random.randrange(1,10000)
    full_file_name = os.path.join(path,str(file_name) + '.jpg')
    #print(full_file_name)
    urllib.request.urlretrieve(image_url,full_file_name)
        
if( len (sys.argv) > 1):
    query = "+".join(sys.argv[1:])
    address = "https://www.pexels.com/search/{}".format(query)
    #webbrowser.open(address)
else:
    query = input("Enter search term ")
    address = "https://www.pexels.com/search/{}".format(query)
    #webbrowser.open(address)

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()  

r  = requests.get(address)
data = r.text
soup = BeautifulSoup(data,"html.parser")
for link in soup.select('.js-photo-link img'):
    name = link.get('srcset')
    len = (name.find('?'))
    newname = name[0:len]
    #print(newname)
    downloader(newname,directory)
#root = tk.Tk()
#root.withdraw()
#directory = filedialog.askdirectory()  #source folder

#url ="http://www.binarynote.com/wp-content/themes/binarynote3/images/main.jpg"
#downloader(link.get(srcset,directory))