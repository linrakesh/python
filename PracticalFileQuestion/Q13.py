# Write a UDF in python, it will take two arguments list
# (sequence of elements) and its size . 
# Replace and display first half elements with second half elements of a list.
# For example:  list elements are:	1	2	3	4	5
# Output is:	4	5	3	1	2

list1 = [1,2,3,4,5]
n = len(list1)
for i in range(n//2):
  list1[i],list1[n//2+1+i]= list1[n//2+1+i],list1[i]
print(list1)
