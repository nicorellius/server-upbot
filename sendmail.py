#! /usr/bin/env python

import smtplib
from sys import argv
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import formatdate

# email smtp settings
with open('/home/nick/dev/prv/serupbot/email_password.txt') as email_password:
    password = email_password.read().strip()
        
sender   = 'admin@basecave.com'
username = 'nicorellius.mail@gmail.com'
server   = 'smtp.gmail.com:587'

def send_mail(subject, recipient, body):
    
    msg            = MIMEMultipart()
    msg['From']    = sender
    msg['To']      = recipient
    msg['Date']    = formatdate(localtime=True)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP(server)
    print('connecetd to %s...' % server)
    smtp.starttls()
    smtp.login(username, password)
    print('logged in to %s...' % server)
    
    try:
        smtp.sendmail(sender, recipient, msg.as_string())
        print('mail sent...')
    
    except smtplib.SMTPException, e:
        print str(e)

    smtp.quit()
    
if __name__ == '__main__':
    
    if 3 > len(argv) > 4:
        print('wrong number of arguments.')
    
    else:
        send_mail(argv[1], argv[2], argv[3])

