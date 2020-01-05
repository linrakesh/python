a = 10
b = int(input("Enter any number "))
try:
    c = a/b
except:
    print('Cannot divide NUMBER by STRING')
else:
    print('Result :', c)
