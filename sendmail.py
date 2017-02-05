#! /usr/bin/env python3

import smtplib
from sys import argv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

# E-mail SMTP settings
with open('/home/nick/dev/prv/serupbot/email_password.txt') as email_password:
    password = email_password.read().strip()
        
sender = 'admin@basecave.com'
username = 'nicorellius.mail@gmail.com'
server = 'smtp.gmail.com:587'


def send_mail(subject, recipient, body):
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP(server)
    print('Connected to {0}...'.format(server))
    smtp.starttls()
    smtp.login(username, password)
    print('Logged in to {0}...'.format(server))
    
    try:
        smtp.sendmail(sender, recipient, msg.as_string())
        print('E-mail sent...')
    
    except smtplib.SMTPException as e:
        print(e)

    smtp.quit()
    
if __name__ == '__main__':
    
    if 3 > len(argv) > 4:
        print('Incorrect number of arguments.')
    
    else:
        send_mail(argv[1], argv[2], argv[3])

