def factorial(n):
    if n==1:
        return 1
    else:
        return n*(factorial(n-1))

#function call 
n = int(input("Enter any number "))
result = factorial(n)
print("factorial of {} is  {} ".format(n,result))