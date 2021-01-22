# program to find out sum of the following series
# sum = X+X2 /!2 + X3 /!3 + n terms
# made by     :
import math
n = int(input('Enter any number  :'))
x = int(input('Enter value of x  :'))
s=0
for i in range(1,n+1):
   s = s+(x**i)/math.factorial(i) 
print('Sum of the series is :',s)