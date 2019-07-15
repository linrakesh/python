# program to download pdf file from any website.
#made by        : rakesh kumar

import urllib.request

def download(tutorialName):
    url = 'https://www.tutorialspoint.com/' + tutorialName + '/' + tutorialName + '_tutorial.pdf'
    #url ="https://cbsetoday.com/wp-content/uploads/2018/05/MYSQL-ASS-4-class-XI.pdf"
    downloadLocation = ''

    pdf = urllib.request.urlopen(url)
    saveFile = open(downloadLocation + tutorialName +  '.pdf', 'wb')  # because pdf is a binary file
    saveFile.write(pdf.read())
    saveFile.close()
    print('Downloaded!')

if __name__ == '__main__':
    while True:
        tutorialName = input('Name of the tutorial pdf to be downloaded: ')
        download(tutorialName)
        choice = input("Do you want to download more PDF(y/n) :")
        if(choice =='n'):
            break