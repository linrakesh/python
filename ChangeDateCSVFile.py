import csv
import xlwt
with open("DOB.csv") as csvfile:
    csv_reader = csv.reader(csvfile)
    wb = xlwt.Workbook()
    ws = wb.add_sheet("DOB")
    ws.write(0,0,"Admno")
    ws.write(0,1,"First")
    ws.write(0,2,"Last")
    ws.write(0,3,"Class")
    ws.write(0,4,"section")
    ws.write(0,5,"DOB")
    i=1
    for line in csv_reader:
        # print(line)
        
        line2 = line[5].split(' ')
        line3= '-'.join(line2)
        #print(line3)
        # print(line2)
        ws.write(i,0,line[0])
        ws.write(i,1,line[1])
        ws.write(i,2,line[2])
        ws.write(i,3,line[3])
        ws.write(i,4,line[4])
        ws.write(i,5,line3)
        i= i+1
    wb.save("dob.xls")
    print("New Excel Sheet generated...............")
