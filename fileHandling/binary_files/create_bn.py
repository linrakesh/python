import pickle
rec=[]
while True:
    roll= int(input('Enter Name :'))
    name=input('Enter your Name : ')
    record = [roll, name]
    rec.append(record)
    choice=input('Add More(Y/N ) ? ')
    if choice.upper() == 'N':
         break
f = open("student", "wb")
pickle.dump(rec, f)
f.close()
