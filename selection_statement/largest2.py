a = int(input('Enter first number :'))
b = int(input('Enter second number :'))
c = int(input('Enter third number :'))
if(a > b and a > c):
    print(a, ' is the largest number')

if(b > a and b > c):
    print(b, ' is the largest number')

if(c > b and c > a):
    print(c, ' is the largest number')
