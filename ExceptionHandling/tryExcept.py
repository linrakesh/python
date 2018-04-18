try:
    a = 10 
    b  = int(input("Enter any number "))
    print(b)
    print(type(b))
    c = a/b
    print(c)
except:
    print('Can not divide NUMBER by STRING')
else:
    print("You are able to divide 10 by your inputed number")