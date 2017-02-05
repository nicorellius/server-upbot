from sys import argv

from googlevoice import Voice
from googlevoice.util import LoginError

# E-mail SMTP settings
with open('/home/nick/dev/prv/serupbot/email_password.txt') as email_password:
    password = email_password.read().strip()


def send(number, message):
    
    USERNAME = 'nicorellius.mail'
    PASSWORD = password
    
    voice = Voice()
    
    try:
        voice.login(USERNAME, PASSWORD)
        
    except LoginError as e:
        print("Error logging into SMS server: {0}".format(str(e)))
    
    # number = input('Number to send message to: ')
    # message = input('Message text: ')
    
    # try:

    voice.send_sms(number, message)
        
    # except Exception as e:
    #     print('Phone number or message error, skipping SMS: {0}'.format(str(e)))
    #     print('Continuing without sending SMS...')

    
# For testing this program can be run at the terminal with args
if __name__ == '__main__':
    
    if len(argv) != 3:
        print('Incorrect number of arguments.')
        
    else:
        send(argv[1], argv[2])
