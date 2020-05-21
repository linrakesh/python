import csv
import xlwt
import tabulate
import re
def writecell(ws,sub,marks,grade,row):
    try:
        subject = int(sub)
        if(subject ==301):                 #english
            ws.write(row,2,int(marks),st1)
            ws.write(row,3,grade,st1)
            l_eng.append(int(marks))
            l_eng.append(grade)
        if(subject==302):                  #hindi
            ws.write(row,4,int(marks),st1)
            ws.write(row,5,grade,st1)
            l_hindi.append(int(marks))
            l_hindi.append(grade)
        if(subject==41):                   #maths
            ws.write(row,6,int(marks),st1)
            ws.write(row,7,grade,st1)
            l_maths.append(int(marks))
            l_maths.append(grade)
        if(subject==42):                   #physics
            ws.write(row,8,int(marks),st1)
            ws.write(row,9,grade,st1)
            l_phy.append(int(marks))
            l_phy.append(grade)
        if(subject==43):                   #chemistry
            ws.write(row,10,int(marks),st1)
            ws.write(row,11,grade,st1)
            l_chem.append(int(marks))
            l_chem.append(grade)
        if(subject==83 or subject==283):   # computer sciece
            ws.write(row,12,int(marks),st1)
            ws.write(row,13,grade,st1)
            l_cs.append(int(marks))
            l_cs.append(grade)
        if(subject==65 or subject==265):   #informatics practices
            ws.write(row,14,int(marks),st1)
            ws.write(row,15,grade,st1)
            l_ip.append(int(marks))
            l_ip.append(grade)
        if(subject==44):                   # Biology
            ws.write(row,16,int(marks),st1)
            ws.write(row,17,grade,st1)
            l_bio.append(int(marks))
            l_bio.append(grade)
        if(subject==48):                   # physical education
            ws.write(row,18,int(marks),st1)
            ws.write(row,19,grade,st1)
            l_pedu.append(int(marks))
            l_pedu.append(grade)
        if(subject==30):                   #30 - economics
            ws.write(row,20,int(marks),st1)
            ws.write(row,21,grade,st1)
            l_eco.append(int(marks))
            l_eco.append(grade)
        if(subject==55):                    #55 - accounts
            ws.write(row,22,int(marks),st1)
            ws.write(row,23,grade,st1)
            l_acc.append(int(marks))
            l_acc.append(grade)
        if(subject==54):                    #54 - Business studies
            ws.write(row,24,int(marks),st1)
            ws.write(row,25,grade,st1)
            l_bst.append(int(marks))
            l_bst.append(grade)
        if(subject==53):                    #837 - Fashion Studuies
            ws.write(row,26,int(marks),st1)
            ws.write(row,27,grade,st1)
            l_fst.append(int(marks))
            l_fst.append(grade)
        if(subject==28):                    #28 - Pol Science
            ws.write(row,28,int(marks),st1)
            ws.write(row,29,grade,st1)
            l_psci.append(int(marks))
            l_psci.append(grade)
        if(subject==34):                    #34 - Hindi Vocal Music
            ws.write(row,30,int(marks),st1)
            ws.write(row,31,grade,st1)
            l_music.append(int(marks))
            l_music.append(grade)
        if(subject==52):                    # 52- comm. art
            ws.write(row,32,int(marks),st1)
            ws.write(row,33,grade,st1)
            l_cart.append(int(marks))
            l_cart.append(grade)
        if(subject==27):                    # 27- History
            ws.write(row,34,int(marks),st1)
            ws.write(row,35,grade,st1)
            l_hist.append(int(marks))
            l_hist.append(grade)
        if(subject==29):                    # 29- GEOGRAPHY
            ws.write(row,36,int(marks),st1)
            ws.write(row,37,grade,st1)
            l_geo.append(int(marks))
            l_geo.append(grade)
        if(subject==37):                    # 37 - PSYCHOLOGY
            ws.write(row,38,int(marks),st1)
            ws.write(row,39,grade,st1)
            l_psy.append(int(marks))
            l_psy.append(grade)
    except:
        return

def writecell2(ws1,l,row):
    st2=xlwt.easyxf('align: horiz centre , vert centre ,wrap yes')

    a1=a2=b1=b2=c1=c2=d1=d2=e=0
    t90=0
    tpass=tpassper=t100=t75=t60=t45=t33=t32=0
    t=len(l)
    
    total=0
    ts=0
    for i in range(0,t,2):
        if l[i]==100:
            t100+=1
        if l[i]>=90:
            t90+=1
        if (l[i]>=75) and ( l[i+1] not in ['FTE','FE']):
            t75+=1
        if (l[i]>=60) and ( l[i+1] not in ['FTE','FE']):
            t60+=1
        if (l[i]>=45 and l[i]<60) and ( l[i+1] not in ['FTE','FE']):
            t45+=1
        if (l[i]>=33 and l[i]<45) and ( l[i+1] not in ['FTE','FE']):
            t33+=1
        if l[i]<=32 or (l[i+1] in ['FTE','FE']) :
            t32+=1
        total+=l[i]
        ts+=1
     
    avgmrk=total/ts
    tpass=ts-t32
    tpassper=tpass*100/ts

    for i in range(1,t,2):
        if l[i]=='A1':
            a1+=1
        if l[i]=='A2':
            a2+=1
        if l[i]=='B1':
            b1+=1
        if l[i]=='B2':
            b2+=1
        if l[i]=='C1':
            c1+=1
        if l[i]=='C2':
            c2+=1
        if l[i]=='D1':
            d1+=1
        if l[i]=='D2':
            d2+=1
        if l[i] in ['FTE','FE']:
            e+=1
    
    ws1.write(row,1,ts,st2)
    ws1.write(row,2,tpass,st2)
    ws1.write(row,3,tpassper,st2)
    ws1.write(row,4,avgmrk,st2)
    ws1.write(row,5,t90,st2)
    ws1.write(row,6,t75,st2)
    ws1.write(row,7,t60,st2)
    ws1.write(row,8,t45,st2)
    ws1.write(row,9,t33,st2)
    ws1.write(row,10,t32,st2)
    ws1.write(row,11,t100,st2)

    ws1.write(row,12,a1,st2)
    ws1.write(row,13,a2,st2)
    ws1.write(row,14,b1,st2)                
    ws1.write(row,15,b2,st2)
    ws1.write(row,16,c1,st2)
    ws1.write(row,17,c2,st2)
    ws1.write(row,18,d1,st2)        
    ws1.write(row,19,d2,st2)
    ws1.write(row,20,e,st2)
                    
file=open("08926.csv","r")
r=csv.reader(file)
wb=xlwt.Workbook()
ws=wb.add_sheet("result")
ws1=wb.add_sheet("result1")

st=xlwt.easyxf('font: bold yes;align: horiz centre , vert centre ,wrap yes')
st1=xlwt.easyxf('align: horiz centre')

# Heading  row of first sheet
ws.write(0,0,"Roll No",st)
ws.write(0,1,"Student Name",st)
ws.write_merge(0,0,2,3,"English",st)
ws.write_merge(0,0,4,5,"Hindi",st)
ws.write_merge(0,0,6,7,"Maths",st)
ws.write_merge(0,0,8,9,"Physics",st)
ws.write_merge(0,0,10,11,"Chemistry",st)
ws.write_merge(0,0,12,13,"CS",st)   
ws.write_merge(0,0,14,15,"IP",st)
ws.write_merge(0,0,16,17,"Bio",st)
ws.write_merge(0,0,18,19,"Physical",st)
ws.write_merge(0,0,20,21,"Eco",st)
ws.write_merge(0,0,22,23,"Account",st)
ws.write_merge(0,0,24,25,"Bst",st)
ws.write_merge(0,0,26,27,"Fst",st)
ws.write_merge(0,0,28,29,"Pol Sci",st)
ws.write_merge(0,0,30,31,"Music",st)
ws.write_merge(0,0,32,33,"CART",st)
ws.write_merge(0,0,34,35,"History",st)
ws.write_merge(0,0,36,37,"Geography",st)
ws.write_merge(0,0,38,39,"Psychology",st)
ws.write(0,40,"result",st)

# Heading row of second sheet
ws1.write(1,0,"English")
ws1.write(2,0,"Hindi")
ws1.write(3,0,"Maths")
ws1.write(4,0,"Physics")
ws1.write(5,0,"Chemistry")
ws1.write(6,0,"Comp. Sci")
ws1.write(7,0,"Infor. Prac.")
ws1.write(8,0,"Biology")
ws1.write(9,0,"Physical Edu.")
ws1.write(10,0,"Economics")
ws1.write(11,0,"Account")
ws1.write(12,0,"Bst")
ws1.write(13,0,"Fst")
ws1.write(14,0,"Plo.Sci.")
ws1.write(15,0,"Music")
ws1.write(16,0,"Com.Art")
ws1.write(17,0,"History")
ws1.write(18,0,"Geography")
ws1.write(19,0,"Psychology")

# Heading col in second sheet

ws1.write(0,0,"Subject",st)
ws1.write(0,1,"Total No. of Student ",st)
ws1.write(0,2,"Passed",st)
ws1.write(0,3,"Passed %",st)
ws1.write(0,4,"Sub Avg Marks",st)
ws1.write(0,5,"Above 90 ",st)
ws1.write(0,6,"above 75 ",st)
ws1.write(0,7,"I Div.   (60 and Above)",st)
ws1.write(0,8,"II Div.    (45-59) ",st)
ws1.write(0,9,"III Div    (33-44).",st)
ws1.write(0,10,"Failed    ( 0-32)",st)
ws1.write(0,11,"100 marks",st)
ws1.write(0,12,"A1  (Grade)",st)
ws1.write(0,13,"A2  (Grade)",st)
ws1.write(0,14,"B1  (Grade)",st)
ws1.write(0,15,"B2  (Grade)",st)
ws1.write(0,16,"C1  (Grade)",st)
ws1.write(0,17,"C2  (Grade)",st)
ws1.write(0,18,"D1  (Grade)",st)
ws1.write(0,19,"D2  (Grade)",st)
ws1.write(0,20,"E   (Grade)",st)


l_eng=[]
l_hindi=[]
l_maths=[]
l_phy=[]
l_chem=[]
l_cs=[]
l_ip=[]
l_bio=[]
l_pedu=[]
l_eco=[]
l_acc=[]
l_bst=[]
l_fst=[]
l_psci=[]
l_music=[]
l_cart=[]
l_hist=[]
l_geo=[]
l_psy=[]

# read csv file 
i=1
line3=[]
for line in r:
    if len(line)>0:
        line1=''.join(line)
        if line1[0].isdigit():
            line2=re.sub(' +',' ',line1)
            line3=line2.split(' ')
            if line3[3].isdigit()==True:
                line3.insert(3,' ')
                line3.insert(4,' ')
            elif line3[4].isdigit()==True:
                line3.insert(4,' ')
            #print(line3)          
            ws.write(i,0,line3[0])
            ws.write(i,1,line3[2]+' '+line3[3]+' '+line3[4])
            writecell(ws,line3[5],line3[6],line3[7],i)
            writecell(ws,line3[8],line3[9],line3[10],i)
            writecell(ws,line3[11],line3[12],line3[13],i)
            writecell(ws,line3[14],line3[15],line3[16],i)
            writecell(ws,line3[17],line3[18],line3[19],i)
            writecell(ws,line3[20],line3[21],line3[22],i)
            ws.write(i,40,line3[len(line3)-2],st1)
            ws.write(i,41,line3[len(line3)-1],st1)
            i=i+1

# write in second sheet

if len(l_eng)>0:
    writecell2(ws1,l_eng,1)
if  len(l_hindi)>0:
    writecell2(ws1,l_hindi,2)
if len(l_maths)>0:
    writecell2(ws1,l_maths,3)
if len(l_phy)>0:
    writecell2(ws1,l_phy,4)
if len(l_chem)>0:
    writecell2(ws1,l_chem,5)
if len(l_cs)>0:
    writecell2(ws1,l_cs,6)
if len(l_ip)>0:
    writecell2(ws1,l_ip,7)
if len(l_bio)>0:
    writecell2(ws1,l_bio,8)
if len(l_pedu)>0:
    writecell2(ws1,l_pedu,9)
if len(l_eco)>0:
    writecell2(ws1,l_eco,10)
if len(l_acc)>0:
    writecell2(ws1,l_acc,11)
if len(l_bst)>0:
    writecell2(ws1,l_bst,12)
if len(l_fst)>0:
    writecell2(ws1,l_fst,13)
if len(l_psci)>0:
    writecell2(ws1,l_psci,14)
if len(l_music)>0:
    writecell2(ws1,l_music,15)
if len(l_cart)>0:
    writecell2(ws1,l_cart,16)
if len(l_hist)>0:
    writecell2(ws1,l_hist,17)
if len(l_geo)>0:
    writecell2(ws1,l_geo,18)
if len(l_psy)>0:
    writecell2(ws1,l_psy,19)
    



wb.save("result123.xls")
print("\n\n\nExcel sheet Generated.....Please check results\n\n\n")


       
file.close()
