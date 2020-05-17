# program to update a record in csv file
import csv
name = input('Name to Delete :')
records = []
found = 0
file = open("student.csv", "r")
reader = csv.reader(file)
for record in reader:
    if(record[1]!= name):
        records.append(record)
        found = 1
    
file.close()

# Remove the old file and create a new csv file
file = open("student.csv", "w")
writer = csv.writer(file,lineterminator='\n')
writer.writerows(records)
file.close()

if(found == 0):
    print(name, " does not exists")
else:
    print(name, " deleted successfully")
