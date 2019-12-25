#   program to find out EMI using formula
#   EMI  = (p*r(1+r)**t)/((1+r)**t-1)
#   made by     : rakesh kumar

from math import pow


def emi_calculate(p, r, t):
    r = r/(12*100)  # rate for one month
    t = t*12  # one month time
    emi = (p*r*pow(1+r, t))/(pow(1+r, t)-1)
    return emi


if __name__ == "__main__":
    p = int(input('Enter pricipal amount :'))
    r = int(input('Enter rate of interest :'))
    t = int(input('Enter time in years :'))
    emi = emi_calculate(p, r, t)

    print('Monthly Installment :%.2f' % emi)
