#   User defined recursive function to find out nth fibonacci number
#   and its implementation in a python program


def fab(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fab(n-1)+fab(n-2)


if __name__ == "__main__":
    for x in range(1, 21):
        print(fab(x), end=" ")
