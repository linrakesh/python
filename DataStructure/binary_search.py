def binary_search(x, first, last, data):
    if(first > last):
        return 0
    else:
        mid = (first+last)//2
        if(x[mid] == data):
            return 1
        if(x[mid] < data):
            return binary_search(x, mid+1, last, data)
        if(x[mid] > data):
            return binary_search(x, first, mid-1, data)


x = [1, 2, 3, 5, 7, 8, 9, 10, 12, 14, 15, 18, 20, 22]
data = 15
first = 0
last = 13

result = binary_search(x, first, last, data)
if(result == 0):
    print("Data not found")
else:
    print("Data found")
