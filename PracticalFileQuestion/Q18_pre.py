#program to create a binary file having records of book in the format
# {'bookno','book_name'}
import pickle

file = open('C:/python/PracticalFileQuestion/book.dat', 'ab')
book ={}
while True:
      no = int(input('Enter book no :'))
      name = input('Enter book no :')
      book['bookno'] = no
      book['book_name'] = name
      pickle.dump(book,file)
      choice = input('Add more books(y/n) :').upper()
      if choice =='N':
        break
file.close()
print('Binary file creation complete.....')
