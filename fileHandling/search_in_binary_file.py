# program to search a name in binary file
#   made by         : rakesh kumar
#   Compiled on     : 8-July-2018

import pickle
name = input('Name  to search :')
file = open("student.dat", "rb")
list1 = pickle.load(file)
file.close()

found = 0
for x in list1:
    if name in x['name']:
        found = 1
print("Found in binary file" if found == 1 else "Not found")
