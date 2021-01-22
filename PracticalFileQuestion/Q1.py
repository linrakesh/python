# program to input marks of 5 subject and calculate total marks and average
# marks of a student
# made by     : 
mark1 = int(input('Enter marks in first subject :'))
mark2 = int(input('Enter marks in second subject :'))
mark3 = int(input('Enter marks in third subject :'))
mark4 = int(input('Enter marks in fourth subject :'))
mark5 = int(input('Enter marks in fifth subject :'))
sum1 = mark1+mark2+mark3+mark4+mark5
avg = sum1/5
print('Total marks  :',sum1)
print('Average marks :',avg)