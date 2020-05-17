# program to update a record in csv file
import csv
name = input('Name to Update :')
records = []
found = 0
file = open("student.csv", "r")
reader = csv.reader(file)
for record in reader:
    if(record[1] == name):
        record[1] = input('New Name:')
        records.append(record)
        found = 1
    else:
        records.append(record)
file.close()

# Remove the old file and create a new csv file
headers = ['rollno', 'name', 'stream', 'fees']
file = open("student.csv", "w")
writer = csv.writer(file, lineterminator='\n')
writer.writerow(headers)
writer.writerows(records)
file.close()

if(found == 0):
    print(name, " does not exists")
else:
    print(name, " updated successfully")
