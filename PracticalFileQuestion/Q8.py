#Write a UDF in python, it will take three arguments list(sequence of elements),
# its size and finding element . Function search and return 1 if element is present
# in the given list otherwise return -1 . Using Binary search
def binary_search(list1,n,data):
    first = 0 
    last = n-1
    found=-1
    while first<=last and found==-1:
          mid = (first+last)//2
          if list1[mid]==data:
            found=1
          elif list1[mid]<data:
              first = mid+1
          else:
              last = mid -1
    return found

#implementation of user defined function
list1=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,20]
n=17
result = binary_search(list1,n,17)
if result ==1:
  print('Number present')
else:
  print('Number not present')