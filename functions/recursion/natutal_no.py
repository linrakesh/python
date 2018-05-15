def natural(n):
    if n ==1:
        print(1)
    else:
        print(n)
        return natural(n-1)
# function call to print 100 natural no
natural(100) 