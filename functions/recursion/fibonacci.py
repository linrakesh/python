#   program to find out nth fibonacci number using recursion
#   made by         : rakesh kumar
#   last compiled   : 20-12-2018


def fibonacci(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


result = fibonacci(30)
print(result)
