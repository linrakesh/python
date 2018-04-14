#-------------------------------------------------------------------------------
# Name:        sending emails
# Purpose:     send emails using gmail
# Author:      rakesh kumar
# Created:     18-04-2017
# Copyright:   binarynote.com
# Licence:     MIT-2.0
#-------------------------------------------------------------------------------
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def mail():
    fromaddr = "rakesh.linux@gmail.com"
    toaddr = "rakeysh.kumar@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "This is a simple message from python"

    body = "Python test mail sending from python program"

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('rakesh.linux@gmail.com','RAMJI00789')
    text = msg.as_string()

    server.sendmail(fromaddr,toaddr,text)

if __name__ == '__main__':
    mail()
