import urllib.request
import random

def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)


url ="http://www.binarynote.com/wp-content/themes/binarynote3/images/main.jpg"
downloader(url)