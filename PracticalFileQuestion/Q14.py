# Write a UDF in python, it will take two arguments list(sequence of elements)
# and its size.	Function arrange and display elements in ascending order.
# Using selection sort.

def insertion_sort(list1):
  n = len(list1)
  for i in range(1,n):
    temp = list1[i]
    j = i-1
    while j>=0 and temp<list1[j]:
          list1[j+1]= list1[j]
          j = j-1
    list1[j+1]= temp
  return list1

# function implementation
list1 = [43,3,1,23,45,45,6,7,8,89,34,78]
list1 = insertion_sort(list1)
print(list1)
