def Linear_Search(l, start, n, value):
    if start < n:
        if l[start] == value:
            return 1
        else:
            return Linear_Search(l, start+1, n, value)
    else:
        return 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = int(input('Enter number to search :'))
n = len(l)-1
result = Linear_Search(l, 0, n, data)
if(result == 1):
    print('data found')
else:
    print('Data not not found')
