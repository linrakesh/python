# Write a menu-driven program implementing user-defined functions to perform 
# different functions on a csv file “student” such as:
# (a)	Write a single record to csv.
# (b)	Write all the records in one single go onto the csv.
# (c)	Display the contents of the csv file.
import csv

def single_record():
  file = open('C:/python/PracticalFileQuestion/student.csv', 'a')
  admno = int(input('Enter admno :'))
  name = input('Enter name :')
  std = input('Enter standard :')
  writer = csv.writer(file,lineterminator='\n')
  writer.writerow([admno,name,std])
  file.close()


def multiple_records():
  file = open('C:/python/PracticalFileQuestion/student.csv', 'a')
  data=[]
  while True:
    admno = int(input('Enter admno :'))
    name = input('Enter name :')
    std = input('Enter standard :')
    data.append([admno,name,std])
    choice= input('Add more records(y/n) :').upper()
    if choice =='N':
      break

  writer = csv.writer(file, lineterminator='\n')
  writer.writerows(data)
  file.close()

def read_csv_file():
  file = open('C:/python/PracticalFileQuestion/student.csv', 'r')
  reader = csv.reader(file)
  for line in reader:
      print(line)
  file.close()

while True:
  print('\n\n CSV File Handling')
  print('1. Write Single Record')
  print('2. Write multiple Records')
  print('3. Read Whole CSV file ')
  print('4. Close Application')
  choice=input('Enter your choice :')
  if choice=='1':
    single_record()
  if choice=='2':
    multiple_records()
  if choice=='3':
    read_csv_file()
  if choice=='4':
    break