
def armstrong(n):
    m = n
    sum = 0
    while(n != 0):
        rem = n % 10
        sum += rem**3
        n = n//10
    return True if sum == m else False


if __name__ == "__main__":
    n1 = int(input('Enter first value  :'))
    n2 = int(input('Enter last value  :'))
    for x in range(n1, n2+1):
        if(armstrong(x)):
            print(x)
