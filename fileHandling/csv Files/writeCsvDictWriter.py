import csv
headers =['rollno','name','stream','fees']
records = [
    {'fees': 2356,'rollno': 12, 'name': 'surendra', 'stream': 'Humanities', },
    {'rollno': 13, 'stream': 'Humanities', 'fees': 2356,'name': 'Ashok', },
    {'rollno':15,'name':'Nipun','stream':'Humanities','fees':2356},
    {'rollno': 22, 'name': 'Ayush Negi', 'fees': 2356,'stream': 'Science', },
]

f = open("student.csv", "w")
writer = csv.DictWriter(f, fieldnames = headers, lineterminator='\n')
writer.writeheader()
writer.writerows(records)
f.close()
print("Check your file now....")
