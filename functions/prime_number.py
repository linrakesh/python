from math import sqrt


def prime_number(n):
    flag = True
    for x in range(2, int(sqrt(n))+1):
        if n % x == 0:
            flag = False
    return flag


if __name__ == "__main__":
    if(prime_number(12)):
        print('Prime Number')
    else:
        print('Not a prime Number')
