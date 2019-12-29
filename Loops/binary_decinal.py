#   program to find out decimal number of any given binary number
#   made by         : rakesh kumar
n = int(input('Enter any number  :'))
sum = 0
i = 0
while n != 0:
    rem = n % 10
    sum = sum+rem*2**i
    n = n//10
    i = i+1

print('Decimal Equivalent :', sum)
