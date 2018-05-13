#-------------------------------------------------------------------------------
# Name:        Bulk Email Sender using Excel file and 
# Purpose:     Program reads name and email Id from Excel file and send to all the members
#
# Author:      rakesh  kumar
#
# Created:     11-02-2018
# Copyright:   rakesh kumar
# Licence:     Private
#-------------------------------------------------------------------------------
import xlrd
import time
import smtplib
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile ="abcd.txt"
fp = open(textfile, 'r')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

me ='rakesh@binarynote.com'
you = 'support@binarynote.com'

msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

password = input("Enter your password")
book = xlrd.open_workbook("phone.xlsx")
sheet = book.sheet_by_index(0)
count = sheet.nrows
for rx in range(1,sheet.nrows):
    rec_email = sheet.cell_value(rx,2)
    rec_name  = sheet.cell_value(rx,0)
    msg['To'] = rec_email
    connection = smtplib.SMTP_SSL('gator3189.hostgator.com',465)
    connection.ehlo()
    #connection.starttls()
    connection.login('rakesh@binarynote.com',password)
    connection.sendmail(me,[rec_email],msg.as_string())
    connection.quit()
    positionStr = "Total : "+str(rx).rjust(4) +" out of  : "+ str(count-1).rjust(4) +" send"
    print(positionStr, end='')
    time.sleep(15)
    print('\b' * len(positionStr), end='', flush=True)
    
print('\n\n Emails pushed...\n\n')