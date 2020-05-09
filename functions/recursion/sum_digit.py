# recursive function to find out sum of digits
# made by   : rakesh kumar


def summ(n):
    if n == 0:
        return 0
    else:
        return(n % 10+summ(n//10))  # 5 + 2 + 1+0


n = int(input("Enter x : "))
result = summ(n)
print("Sum of digits : ", result)
