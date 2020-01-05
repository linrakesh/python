a = int(input('Enter first number :'))
b = int(input('Enter second number :'))
c = int(input('Enter third number :'))
lar = a
if(lar < b):
    lar = b
if(lar < c):
    lar = c
print(lar, ' is the largest number')
