# Write a menu-driven program to perform all the basic operations using dictionary on student
#  binary file such as inserting,reading, updating, searching and deleting a record.

import pickle
import os


def insert_record():
  file = open('C:/python/PracticalFileQuestion/binary.dat', 'ab')
  admno = int(input('Enter admno :'))
  name = input('Enter name :')
  std = input('Enter standard :')
  student={'admno':admno,'name':name,'std':std}
  pickle.dump(student,file)
  file.close()
  print('Record added successfully........')


def read_records():
  file = open('C:/python/PracticalFileQuestion/binary.dat', 'rb')
  while True:
    try:
      data = pickle.load(file)
      print(data)
    except:
      break
  file.close()


def delete_record():
  file = open('C:/python/PracticalFileQuestion/binary.dat', 'rb')
  temp = open('temp.dat', 'wb')
  tadmno = int(input('Enter admission no to delete :'))
  while True:
    try:
      data = pickle.load(file)
      if data['admno'] != tadmno:
        pickle.dump(data, temp)
    except:
      break
  file.close()
  temp.close()
  os.remove('C:/python/PracticalFileQuestion/binary.dat')
  os.rename('temp.dat', 'C:/python/PracticalFileQuestion/binary.dat')
  print('Record updated......')


def update_record():
  file = open('C:/python/PracticalFileQuestion/binary.dat', 'rb')
  temp = open('temp.dat','wb')
  tadmno = int(input('Enter admission no to update :'))
  while True:
    try:
      data = pickle.load(file)
      if data['admno']==tadmno:
         data['name'] = input('Enter new name :')
         data['std'] = input('Enter new standard :')
      pickle.dump(data,temp)
    except:
      break
  file.close()
  temp.close()
  os.remove('C:/python/PracticalFileQuestion/binary.dat')
  os.rename('temp.dat', 'C:/python/PracticalFileQuestion/binary.dat')
  print('Record updated......')


def search_record():
  file = open('C:/python/PracticalFileQuestion/binary.dat', 'rb')
  tadmno = int(input('Enter admno to search :'))
  found=0
  while True:
    try:
      data = pickle.load(file)
      if data['admno']==tadmno:
         found =1
    except:
      break
  file.close()
  print('Record found ' if found==1 else 'Record not found ')

while True:
  print('\n\n Binary File Handling')
  print('1. Insert Record')
  print('2. Delete Records')
  print('3. Update Record ')
  print('4. Search Record ')
  print('5. Read all Records ')
  print('6. Close Application')
  choice = input('Enter your choice :')
  if choice == '1':
    insert_record()
  if choice == '2':
    delete_record()
  if choice == '3':
    update_record()
  if choice == '4':
    search_record()
  if choice== '5':
    read_records()
  if choice== '6':
    break
