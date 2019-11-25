#   python program to search a word in a text File
#   program by          : rakesh kumar

word = input('Enter any word that you want to find in text File :')
word1= '"'+word+'"'
word2= "'"+word+"'"
f = open("rakesh.txt","r")
data = f.read().split()
if word in data or word1 in data or word2 in data:
    print('Word Found in Text File')
else:
    print('Word not found in Text File')
