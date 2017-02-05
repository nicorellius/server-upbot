from sys import argv

from googlevoice import Voice
from googlevoice.util import LoginError

# change in production
from serupbot.settings.nick import EMAIL_PASSWORD, EMAIL_HOST_USER


def send(number, message):
    
    user = EMAIL_HOST_USER
    password = EMAIL_PASSWORD
    
    voice = Voice()
    
    try:
        voice.login(user, password)
        
    except LoginError, e:
        print("error logging into sms server: {0}".format(str(e)))
    
    # number = input('Number to send message to: ')
    # message = input('Message text: ')
    
    try:
        voice.send_sms(number, message)
        
    except Exception, e:
        print('phone number or message error, skipping sms... {0}'.format(str(e)))
        print('continuing without sending sms...')

    
# for testing this script can be run at the terminal with args
if __name__ == '__main__':
    
    if len(argv) != 3:
        print('wrong number of arguments.')
        
    else:
        send(argv[1], argv[2])