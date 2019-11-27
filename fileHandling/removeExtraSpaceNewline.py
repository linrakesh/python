import re

file = open("abcd.txt")
data = file.read()
data = re.sub('[ \t\n]+', ' ', data)
print(data)
