import json
import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=2121032f088e4370affe13ca317f8d1a')
response = requests.get(url)

#source = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = json.loads(response.text)

for article in data['articles']:
    print(article['author'], end="-")
    print(article['title'])
