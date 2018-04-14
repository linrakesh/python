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
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo()
connection.starttls()
connection.login('rakesh.linux@gmail.com','RAMJI00789')
connection.sendmail('rakesh.linux@gmail.com','rakeysh.kumar@gmail.com','SUBJECT: This is demo \n\n This is a mail from python')
connection.quit()
print('Email pushed...')