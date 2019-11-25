def upto9(a):
     if a==1:
          print("One  ",end="")
     elif a==2:
          print("Two",end="")
     elif a==3:
          print("Three ",end="")
     elif a==4:
          print("Four ",end="")
     elif a==5:
          print("Five ",end="")
     elif a==6:
          print("Six ",end="")
     elif a==7:
          print("Seven ",end="")
     elif a==8:
          print("Eight ",end="")
     elif a==9:
          print("Nine ",end="")
     
def upto20(a):
     if a==10:
          print("Ten ")
     elif a==11:
          print("Eleven  ",end="")
     elif a==12:
          print("Twelve",end="")
     elif a==13:
          print("Thirteen",end="")
     elif a==14:
          print("Fourteen ",end="")
     elif a==15:
          print("Fifteen ",end="")
     elif a==16:
          print("Sixteen ",end="")
     elif a==17:
          print("Seventeen ",end="")
     elif a==18:
          print("Eighteen ",end="")
     elif a==19:
          print("Nineteen ",end="")
     
def upto90(a):
     if ab==0:
          print("Zero",end="")
     elif a==2:
          print("Twenty",end="")
     elif a==3:
          print("Thirty",end="")
     elif a==4:
          print("Fourty ",end="")
     elif a==5:
          print("Fifty",end="")
     elif a==6:
          print("Sixty",end="")
     elif a==7:
          print("Seventy",end="")
     elif a==8:
          print("Eighty",end="")
     elif a==9:
          print("Ninety",end="")
     
     
def crr(ab):
     if ab==0:
          print("Zero",end="")
     if ab<100 and ab>20:
          upto90(ab//10)
          upto9(ab%10)
     if ab<=20 and ab>=10:
          upto20(ab)
     if ab<11:
          upto9(ab)

ab=0    
nx=(input(" Values Here " ))
if len(nx)==9:
     ab=int(nx[0:2])
     crr(ab)
     nx=nx[2:]
     print("Crors" ,end="")
if len(nx)==8:
     ab=int(nx[0])
     crr(ab)
     nx=nx[1:]
     print("Cror",end="")

if len(nx)==7:
     ab=int(nx[0:2])
     crr(ab)
     nx=nx[2:]
     print("Lakhs",end="")
if len(nx)==6:
     ab=int(nx[0])
     crr(ab)
     nx=nx[1:]
     print("Lakh",end="")
     
if len(nx)==5:
     ab=int(nx[0:2])
     crr(ab)
     nx=nx[2:]
     print("Thousends",end="")
if len(nx)==4:
     ab=int(nx[0])
     crr(ab)
     nx=nx[1:]
     print("Thousend",end="")
if len(nx)==3:
     ab=int(nx[0])
     upto9(ab)
     print("Hundreds ",end="")
     nx=nx[1:]
ab=int(nx)
upto90(ab//10)
upto9(ab%10)



