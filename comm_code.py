# purpose       : write a program to read a list and convert that list into comma seperated string 
# author        : rakesh kumar
# licence       : MIT
spam =['apples','banana','oranges','mango','kivi','cheeku','pine apple','strawberries']
string =''
n = len(spam)
for i in range(1,n):
    if i == n-1:
        string +='and '+spam[i]
    else:
        string += spam[i] +","
print('Your new string is : ', string)