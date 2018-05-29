import csv
import xlwt
from tabulate import tabulate
import re
def writecell(ws,sub,marks,row):
    try:
        subject = int(sub)
        if(subject ==101):                 #english
            ws.write(row,2,int(marks))
        if(subject==85):                   #hindi
            ws.write(row,3,int(marks))
        if(subject==41):                   #maths
            ws.write(row,4,int(marks))
        if(subject==86):                   #science
            ws.write(row,5,int(marks))
        if(subject==122):                   #sanskrit
            ws.write(row,6,int(marks))
        if(subject==87):                   #Social Science
            ws.write(row,7,int(marks))
        if(subject==34):                   #music
            ws.write(row,8,int(marks))
    except:
        return

with open('ten_08849.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile)
    wb = xlwt.Workbook()
    ws = wb.add_sheet("result")
    ws.write(0,0,"Roll No")
    ws.write(0,1,"Student Name")
    ws.write(0,2,"Eng")
    ws.write(0,3,"Hindi")
    ws.write(0,4,"Maths")
    ws.write(0,5,"Science")
    ws.write(0,6,"Sanskrit")
    ws.write(0,7,"Social Science")
    ws.write(0,8,"Music")
    i=1
    for line in csv_reader:
        line1 = ''.join(line)
        line2 = re.sub(' +',' ',line1)
        line3 = line2.split(' ')
        # print(line3)
        # print(line3[0],line3[1],line3[2],line3[4],line3[5],line3[7],line3[8],line3[10],line3[11],line3[13],line3[14],line3[16],line3[17],line3[19],line3[20])
        # # for i in line3:
        # #     print(i, end=" ")
        # # print();
        # print(line)
        ws.write(i,0,line3[0])
        ws.write(i,1,line3[1]+' '+line3[2])
        writecell(ws,line3[4],line3[5],i)
        writecell(ws,line3[7],line3[8],i)
        writecell(ws,line3[10],line3[11],i)
        writecell(ws,line3[13],line3[14],i)
        writecell(ws,line3[16],line3[17],i)
        # writecell(ws,line3[19],line3[20],i)
        # print(type(line3[19]),line3[19])

        # if int(line3[4])==301:
        #    ws.write(i,2,int(line3[5]))
        # if int(line3[4])==302:
        #    ws.write(i,3,int(line3[5]))
        i+=1
    wb.save("result.xls")
print("\n\n\nExcel sheet Generated.....Please check results\n\n\n")