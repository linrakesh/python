import zerosms
import getpass
import xlrd
import time
def sendsms():
    # 
    # your_number = getpass.getpass("Enter your phone No. ")
    # your_password = getpass.getpass("Enter your password")
    your_number = '9871816901'
    your_password = 'mypassword'

    book = xlrd.open_workbook("phone.xlsx")
    sheet = book.sheet_by_index(0)
    for rx in range(1,sheet.nrows):
        rec_phone = str(int(sheet.cell_value(rx,1)))
        rec_name  = sheet.cell_value(rx,0)
        msg ="Hello " + rec_name + " This is python generated sms and I love this script to send automated message to all my friend in my list"
        zerosms.sms(phno=your_number,passwd=your_password,message=msg,receivernum=rec_phone)
        time.sleep(10)

sendsms()