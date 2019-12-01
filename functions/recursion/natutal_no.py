def natural(n):
    if n ==1:
        print(1)
    else:
        print(n)
        return natural(n-1)


def natural1(n):
    if n == 100:
        print(100)
        return
    else:
        print(n)
        return natural(n+1)
# function call to print 100 natural no


# function call to print 100 natural no

natural(1)
#natural(100) 

