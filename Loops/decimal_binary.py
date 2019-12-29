#   program to find out binary equivalent of any decimal number
#   made by         : rakesh kumar

n = int(input('Enter any number :'))
l = ''
while(n != 0):
    l = str(n % 2) + l
    n = n//2

print(l)
