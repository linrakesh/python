#   Program of select a random word from a text file dictionary
#   each line contains only a single word
#   program by          : rakesh kumar
#   website             : https://cbsetoday.com

import random as r
with open("sowpods.txt") as file:
    data = file.read().split()
    number = r.randint(0, len(data))
    print(data[number])
