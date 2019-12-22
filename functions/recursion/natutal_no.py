def natural(n):
    if n == 100:
        print(100, end=" ")
        return
    else:
        print(n, end="  ")
        return natural(n+1)


# function call to print 100 natural no
natural(1)
