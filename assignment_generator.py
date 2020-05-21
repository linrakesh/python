
import random

unique=[]
count=1
while True:
    a = random.randint(0,5)
    if a in unique:
        continue
    else:
        unique.append(a)
        count = count+1
    if(count>=7):
        break
# print(unique)

# a,b,c,d,e,f = 2,4,7,9,1,6
operators=['*','/','+','-','**','//']

assignment = "a,b,c,d,e,f = 2,4,7,9,1,6"

print("Assignment-1")

print("Lets assume the values of ",assignment," \n Try to run the following expressions and find out the outputs")

for i in range (1,21):
    string ="Q"+str(i)+". = "
    counter= 0
    while True:
        value =  chr(96+random.randint(1,6))
        # print(value)
        if string.find(value) !=-1 :
            continue
        else:
            string += chr(96+random.randint(1,6))    
            operator = operators[unique[counter]]
            counter += 1
            if(counter<=5):
                string += operator  
        
        if(counter>=6):
            break
        
    print(string)
