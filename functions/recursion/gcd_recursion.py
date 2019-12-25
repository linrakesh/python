def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    a = int(input('Enter first number '))
    b = int(input('Enter second number '))
    result = gcd(a, b)
    print('GCD of {} and {} is {}'.format(a, b, result))
