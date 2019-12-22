try:
    a = 10
    b = int(input("Enter any number "))
    if b == 0:
        raise Exception
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Can not divide NUMBER by STRING')
except Exception as e:
    print('You are trying to divide a number by zero')
else:
    print("You are able to divide 10 by your inputed number")
finally:
    print('This is finally in exception handling')
