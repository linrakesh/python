#   program to create a binary file of records - Just like structure
#   made by         : rakesh kumar
#   Compiled on     : 27-Nov-2019

import pickle
list1 = []
while True:
    roll = input("Enter student Roll No:")
    sname = input("Enter student Name :")
    student = {"roll": roll, "name": sname}
    list1.append(student)
    choice = input("Want to add more record(y/n) :")
    if(choice == 'n'):
        break

file = open("student.dat", "wb")
pickle.dump(list1, file)
file.close()
