# menu drive program to calculate areas 
# made by     :

while True:
  print(' Menu ')
  print("1.  Area of Circle")
  print("2.  Area of Square")
  print("3.  Area of Rectangle")
  print("4.  Exit")
  choice = int(input('Enter your choice :'))
  if choice ==1:
    r = int(input('Enter radius :'))
    area = 3.14*r**2
    print('Area of Circle :',area)
  if choice==2:
    side = int(input('Enter side of square :'))
    area = side*side
    print('Area of square :', area)
  if choice == 3:
    l = int(input('Enter Length :'))
    h = int(input('Enter height :'))
    area = l*h
    print('Area of Rectangle :', area)
  if choice ==4:
    break