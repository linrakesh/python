# program to define lambda function in python


def f(x): return x**2


# lambda function with map() function
l1 = [1, 2, 4, 5, 6, 7, 78, 7, 4, 34, 4, 14, 44, 4, 4]
result = map(f, l1)
print(result)
