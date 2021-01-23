# Write a function in PYTHON to search for a BookNo from a binary file 
# “BOOK.DAT”, assuming the binary file is containing the records of the
#  following type: ("BookNo", "Book_name"). 
# Assume that BookNo is an integer.
import pickle

tno = int(input('Enter book no to search :'))
file = open('C:/python/PracticalFileQuestion/book.dat', 'rb')
found=0
while True:

    try:
      data = pickle.load(file)
      if data['bookno']==tno:
        found=1
        print(data)
    except:
      break
file.close()
print("Book found" if found==1 else "Book Not Found")
