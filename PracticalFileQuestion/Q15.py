# Write a function in PYTHON that counts the number of “Me” or “My” words present in a 
# text file “DIARY.TXT”. If the “DIARY.TXT” contents are as follows:
# My first book was Me and My Family. It gave me chance to be Known to the world.
# The output of the function should be:
# Count of Me/My in file: 4

def count_me_my():
  file = open('C:/python/PracticalFileQuestion/diary.txt', 'r')
  data = file.read().split()
  count = data.count('Me') +data.count('me') + data.count('My')+data.count('my')
  file.close()
  print('Count of me or My :',count)
  
#function call
count_me_my()