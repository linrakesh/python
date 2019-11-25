#       program to scrap examveda.com for questions and their answers.
#       Written by              :   rakesh kumar
#       Last modified on        :   04-august-2019
import os
import requests
from bs4 import BeautifulSoup


def soup_data(url):
    source = requests.get(url, 'lxml').text
    soup = BeautifulSoup(source, 'lxml')
    print(soup.prettify())


if __name__ == "__main__":
    url = "https://www.setaswall.com/samsung-galaxy-a50-wallpapers/"
    print("Process Begins....")
    soup_data(url)
    # for no in range(2, 15):
    #     url = "https://www.setaswall.com/samsung-galaxy-a50-wallpapers/" + \
    #         +str(no)
    #     print(url)
    #     soup_data(url)
    print("Please check your files")
