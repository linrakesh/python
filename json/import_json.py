import json
import requests
source = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(source.read())
