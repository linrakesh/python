#   python program to demonstrate the use of kwargs arguments in pyhon
#   made by             : rakesh kumar


def sum_kwargs(**kwargs):
    for x, y in kwargs.items():
        print('{} and its valiue {}'.format(x, y))


if __name__ == "__main__":
    sum_kwargs(name='rakesh', school='DAV', salary=50000)
