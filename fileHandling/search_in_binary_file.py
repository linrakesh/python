# program to read a binary file of records - Just like structure
#   made by         : rakesh kumar
#   Compiled on     : 8-July-2018

import pickle

name = input('Enter name that you want to search in binary file :')

file = open("student.dat", "rb")
list = pickle.load(file)
file.close()

found = 0
for x in list:
    if name in x['name']:
        found = 1
print("Found in binary file" if found == 1 else "Not found")
