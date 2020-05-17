def hello():
    for x in range(10):
        print('hello', x, end =" ")

def sum_digit(n):
    sum1 = 0
    while n!=0:
        sum1 += n%10
        n = n//10
    return sum1

def simple_interest(p,r,t):
    return p*r*t/100

def area_triangle(base,height):
    return base*height

def isPrime(n):
    found =0
    for x in range(2,(n//2)+1):
        if n%x==0:
            found=1
    return found