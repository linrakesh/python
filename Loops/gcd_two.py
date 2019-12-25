#   program to find out GCD of two number using iterative method
#   made by     : rakeseh kumar


a = int(input('Enter any number'))
b = int(input('Enter another number'))

""" if(a > b):
    number = a
    divider = b
else:
    number = b
    divider = a """

rem = a % b

while(rem != 0):
    a = b
    b = rem
    rem = a % b

print('Your GCD is :', b)
