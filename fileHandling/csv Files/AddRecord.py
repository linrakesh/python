import csv

rollno= int(input('Roll No :'))
name  = input('Name :')
stream = input('Stream :')
fees =  int(input('Fees :'))

records = [rollno,name,stream,fees]

f = open("student.csv", "a")
csvwriter = csv.writer(f, lineterminator='\n')
# csvwriter.writerow(header)
csvwriter.writerow(records)
f.close()
print("Record added ...")
