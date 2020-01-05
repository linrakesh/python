import math as m


def check_prime(n):
    flag = True
    for x in range(2, n//2):
        if n % x == 0:
            flag = False

    return flag

if __name__ == "__main__":
    n = int(input('Enter any integer number  : '))
    result = check2_prime(n)
    print("Prime Number " if (result) else '"Not prime Number')
