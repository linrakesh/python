# Write a function EUCount() in PYTHON, which should read each character
# of a text file IMP.TXT, should count and display the occurrences of 
# alphabets E and U (including small cases e and u too).

def EUcount():
  file = open('C:/python/PracticalFileQuestion/diary.txt', 'r')
  count = 0
  for x in file.read():
      if x in 'EeUu':
        count+=1
  file.close()
  print('Total E or U in file :',count)

#function implementation
EUcount()