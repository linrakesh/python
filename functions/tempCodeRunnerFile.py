#   program to find out sum of element of a list using recursion
#   made by         : rakesh kumar


def sum_element(l):
    if(len(l) == 1):
        return l[0]
    else:
        value = l.pop()
        return value+sum_element(l)


if __name__ == "__main__":

    list1 = [1, 2, 34, 5, 6]
    result = sum_element(list1)
    print('sum of element :', result)
