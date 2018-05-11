#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     11-02-2018
# Copyright:   (c) acer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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
you = 'archana@binarynote.com'

msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you


connection = smtplib.SMTP_SSL('gator3189.hostgator.com',465)
connection.ehlo()
#connection.starttls()
password = input("Enter your password")
connection.login('rakesh@binarynote.com',password)
connection.sendmail(me,[you],msg.as_string())
connection.quit()
print('\n\n Email pushed...\n\n')