# Write a program in python ,count # and display the number 
# of vowels, consonants , uppercase, lowercase characters in string.
string ='''This is me and this is a wonderful Team of India. 
          right now they are playing with only Team australia'''
vowels=0
consonent=0
uppercase=0
lowercase=0
for x in string:
   if x in 'aeiouAEIOU':
      vowels+=1
   else:
      consonent+=1
   if x.isupper():
      uppercase+=1
   else:
      lowercase+=1
print('Total vowels :',vowels) 
print('Total consonent :',consonent) 
print('Total upparcase char :',uppercase) 
print('Total lowercase char : :',lowercase) 