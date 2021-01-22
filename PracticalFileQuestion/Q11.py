#Write a program in python, to create a number list. 
# Calculate and display sum of those elements whose last digit is 5.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 20]
s=0
for x in list1:
    if x%10==5:
       s= s+x
print(' Sum of digits having 5 at the last position :',s)
