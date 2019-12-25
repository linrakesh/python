# python program to download wikipedia page
# made by       : rakesh kumar


import requests
req = requests.post('https://binarynote.com', data={'search': 'wordpress'})
req.raise_for_status()
with open('wordpress.html', 'wb') as fd:
    for chunk in req.iter_content(chunk_size=50000):
        fd.write(chunk)

print("File generated...")
