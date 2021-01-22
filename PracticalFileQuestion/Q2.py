# program to input total unit of electricity consumed and calculate bill
# made by     :
unit= int(input('Enter Total Units :'))
bill=0
if unit<=100:
   bill = unit*1.00
elif unit>100 and unit<=200:
   bill = 100+(unit-100)*2.00
else:
  bill = 300+(unit-300)*4.00
print('Your Bill is :', bill)