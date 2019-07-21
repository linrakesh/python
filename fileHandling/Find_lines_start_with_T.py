#program to find out total number of "Project" word in any given test file 
#made by        : rakesh kumar
# made on       : 07/07/2018   

file =  open(r"abcd.txt",'r')
count=0;
for line in file.readlines():
    if line[0]=='T':
        count+=1
file.close()
print("Total lines that start with alphabet 'T'  :",count)