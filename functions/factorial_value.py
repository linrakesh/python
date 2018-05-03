def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print("Factorial of ", n ," is :",fact)

#function call 
n = int(input("Enter any number "))
factorial(n)