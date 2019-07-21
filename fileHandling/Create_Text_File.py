#program to create Text File using Python
#   made by             : rakesh kumar
#   Last Compiled on    : 7/7/2018

file = open("Testing.txt","w")
file.write("This is rakesh and this is my first file handling program in Python \n")
file.write("This is second line and i am learning new things in pythin")
file.writelines("third line of the same program")
file.close()
print("File Generated please check")