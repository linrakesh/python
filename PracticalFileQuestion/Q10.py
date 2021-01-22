# Write a program in python, to create a number list. Search and display 
# largest and smallest number present in a list . Without using built-in function
list1=[]
while True: 
  a = int(input('Enter any number :'))
  list1.append(a)
  choice=input('Add more number(y/n) :').upper()
  if choice =='N':
    break

lar=low=list1[0]
for x in list1:
    if x >lar:
       lar = x
    if x<low:
      low=x
print('Number list is ', list1)
print('Largest no :',lar)
print('Lowest no :',low)

