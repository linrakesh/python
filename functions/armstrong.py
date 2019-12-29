
def armstrong(n):
    m = n
    sum = 0
    while(n != 0):
        rem = n % 10
        sum += rem**3
        n = n//10
    return True if sum == m else False


if __name__ == "__main__":
    n = int(input('Enter any number :'))
    print('ArmStrong Number ' if(armstrong(n)) else 'Not a Arm Strong Number ')
