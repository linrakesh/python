#   program to find out factorial of any number n using looping method
# made by        : rakesh kumar

n = int(input('Enter any number n: '))
fact = 1
for i in range(1, n+1):
    fact *= i

print('Factorial of {} is {}'.format(n, fact))
