#program to find out total number of "Project" word in any given test file 
#made by        : rakesh kumar
# made on       : 07/07/2018   

file =  open(r"abcd.txt",'r')
words=lines=0
for line in file.readlines():
    lines+=1
    words+=len(line.split())
file.close()
print("Total Words in this File  :",words)
print("Total Lines in this File  :",lines)
