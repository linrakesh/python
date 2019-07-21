#program to read a binary file of records - Just like structure
#   made by         : rakesh kumar
#   Compiled on     : 8-July-2018

import pickle
file = open("student.dat","rb")
list = pickle.load(file)
print(list)
file.close()