#   program to create a binary file of records - Just like structure
#   made by         : rakesh kumar
#   Compiled on     : 8-July-2018

import pickle
list =[]
while True:
    roll = input("Enter student Roll No:")
    sname  = input("Enter student Name :")
    student = {"roll":roll,"name":sname}
    list.append(student)
    choice= input("Want to add more record(y/n) :")
    if(choice=='n'):
        break

file = open("student.dat","wb")
pickle.dump(list,file)
file.close()