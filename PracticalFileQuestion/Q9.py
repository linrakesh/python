# Write a program in python, to input a string check and display given string 
# is a palindrome or not.

string = input('Enter any string : ')
if string == string[-1::-1]:
  print('Palindrome string ')
else:
  print('Not a palindrome string')
