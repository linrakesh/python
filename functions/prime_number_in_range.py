#   program to print the prime numbers between a range of numbers.
#   made by         : rakesh kumar


def check_prime(n):
    flag = True
    for x in range(2, n//2):
        if n % x == 0:
            flag = False

    return flag


if __name__ == "__main__":
    n1 = int(input('Enter the starting number : '))
    n2 = int(input('Enter the Ending number number : '))

    print('Prime Number between :')
    for x in range(n1, n2+1):
        result = check_prime(x)
        if result:
            print(x, end=" ")
