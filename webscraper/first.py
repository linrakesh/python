import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#print(res.text)
file = open("abcd.txt","w")
file.write(res.text)
file.close()