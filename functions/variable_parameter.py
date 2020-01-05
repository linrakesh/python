#   function to demonstrate the workin of args and kwards paramater
#   made by         : rakesh kumar


def sum_values(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


if __name__ == "__main__":
    res = sum_values(1, 2, 3, 4, 5, 6, 7, 8, 9)
    print('Sum of values :', res)
