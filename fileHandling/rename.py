# program to rename all files in a folder
# made by               :   rakesh kumar
# Developed for         :   https://binarynote.com

import os
os.chdir('e://sam')
#print(os.getcwd())
count =1 

def increment():
    global count 
    count = count+1

for f in os.listdir():
    f_name,f_ext = os.path.splitext(f)
    f_name ='binarynotes' +'-'+str(count)
    increment()
    new_name = '{}{}'.format(f_name,f_ext)
    os.rename(f,new_name)
print('Job Completed. Now check your folder!!!')