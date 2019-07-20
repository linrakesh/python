#   program to search an element from a list of different type of values
#   Developed by        : rakesh kumar
#   Last revised on     : 20-lujy-2019

list =[10,20,'a','abc',40,50.6]
a = input("Enter any number")
try:                # if we are able to type cast the value
    b  = eval(a)
    if b in list:
        print("found")
    else:
        print("not found")
except:             # if some run time error occur while conversion
    if a in list:
        print("Found")
    else:
        print("not  found")
