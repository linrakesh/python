def binarySearch(l, start, end, value):
    if start > end:
        return -1
    else:
        mid = (start+end)//2
        if l[mid] == value:
            return mid
        elif data < l[mid]:
            return binarySearch(l, start, mid-1, value)
        else:
            return binarySearch(l, mid+1, end, value)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
end = len(l)-1
data = 6
result = binarySearch(l, 0, end, data)
if(result != -1):
    print('Result found at index {}'.format(result))
else:
    print('Data not not found')
