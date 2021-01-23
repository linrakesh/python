#Write a function in PYTHON to read the contents of a text file “Places.Txt” 
# and display all those lines on screen which are either starting with ‘P’ or with ‘S’.
def line_count():
  file = open('C:/python/PracticalFileQuestion/diary.txt', 'r')
  count =0
  for line in file.readlines():
      if line[0]=='P' or line[0]=='S':
        count+=1
        print(line) 
  file.close()
  print('Total lines :',count)

#function implementation
line_count()
