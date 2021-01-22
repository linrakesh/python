# program to check of primality
# made by     :
n = int(input('Enter any number :'))
found=0
for i in range(2,n//2+1):
    if n%i==0:
      found=1
if found ==0:
  print('Number is prime')
else:
  print('Number is not prime')