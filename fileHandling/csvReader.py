import csv
import xlwt
from tabulate import tabulate
import re
def writecell(ws,sub,marks,row):
    try:
        subject = int(sub)
        if(subject ==301):                 #english
            ws.write(row,2,int(marks))
        if(subject==302):                  #hindi
            ws.write(row,3,int(marks))
        if(subject==41):                   #maths
            ws.write(row,4,int(marks))
        if(subject==42):                   #physics
            ws.write(row,5,int(marks))
        if(subject==43):                   #chemistry
            ws.write(row,6,int(marks))
        if(subject==83):                   # computer sciecen
            ws.write(row,7,int(marks))
        if(subject==65):                   #informatics practices
            ws.write(row,8,int(marks))
        if(subject==44):                   # Biology
            ws.write(row,9,int(marks))
        if(subject==48):                   # physical education
            ws.write(row,10,int(marks))
        if(subject==30):                   #30 - economics
            ws.write(row,11,int(marks))
        if(subject==55):                    #55 - accounts
            ws.write(row,12,int(marks))
        if(subject==54):                    #54 - Business studies
            ws.write(row,13,int(marks))
        if(subject==783):                    #783 - marketing
            ws.write(row,14,int(marks))
        if(subject==28):                    #28 - Pol Science
            ws.write(row,15,int(marks))
        if(subject==34):                    #34 - Hindi Vocal Music
            ws.write(row,16,int(marks))
        if(subject==49):                    #30 - painting
            ws.write(row,17,int(marks))
        if(subject==74):                    #30 - painting
            ws.write(row,18,int(marks))
    except:
        return

with open('raju.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile)
    wb = xlwt.Workbook()
    ws = wb.add_sheet("result")
    ws.write(0,0,"Roll No")
    ws.write(0,1,"Student Name")
    ws.write(0,2,"Eng")
    ws.write(0,3,"Hindi")
    ws.write(0,4,"Maths")
    ws.write(0,5,"Physics")
    ws.write(0,6,"Chemistry")
    ws.write(0,7,"CS")   
    ws.write(0,8,"IP")
    ws.write(0,9,"Bio")
    ws.write(0,10,"Physical")
    ws.write(0,11,"Eco")
    ws.write(0,12,"Account")
    ws.write(0,13,"BS")
    ws.write(0,14,"Marketing")
    ws.write(0,15,"Political")
    ws.write(0,16,"Music")
    ws.write(0,17,"painting")
    ws.write(0,18,"Legal Studies")
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
        writecell(ws,line3[19],line3[20],i)
        # print(type(line3[19]),line3[19])

        # if int(line3[4])==301:
        #    ws.write(i,2,int(line3[5]))
        # if int(line3[4])==302:
        #    ws.write(i,3,int(line3[5]))
        i+=1
    wb.save("result.xls")
print("\n\n\nExcel sheet Generated.....Please check results\n\n\n")