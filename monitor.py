#! /usr/bin/env python3

"""monitor.py: general purpose yet simple server monitoring routine."""

# import threading
import smtplib

import urllib.request

from sys import argv
from socket import socket
from time import asctime

from sendmail import send_mail
from sendsms import send
from util import get_timestamp


# class MonitorTimerManager:
#
#     def fire(self, monitor_test, frequency):
#         monitor_test
#
#         # call fire() again in 60 seconds
#         threading.Timer(frequency, self.fire).start()
#
#         # start calling fire now and every 60 sec thereafter
#         # fire(frequency)


# class MonitorTestManager:


def tcp_test(server_info):
    """
    tcp test

    :param server_info: server ip or hostname with port
    """

    try:
        cpos = server_info.find(':')

    except Exception as e:
        print('server info exception: {0}'.format(str(e)))

    try:
        sock = socket()
        sock.connect((server_info[:cpos], int(server_info[cpos + 1:])))
        # sock.close
        print('tcp_test successful')

    except Exception as e:
        print('socket exception: {0}'.format(str(e)))

    return


def http_test(server_info):
    """
    http test

    :param server_info: server ip or hostname with port, including `http://`
    :returns: boolean value
    """

    user_agent = ''
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(server_info, None, headers)
    response = urllib.request.urlopen(request)

    try:
        data = response.read()
        print('HTTP test successful')

        return data

    except Exception as e:
        print('HTTP test error: {0}'.format(str(e)))


def server_test(test_type, server_info):
    """
    run server test

    :param test_type: test type, eg, tcp or http
    :param server_info: server ipor hostname with port
    :returns: result object
    """

    try:
        if test_type.lower() == 'tcp':
            # result = tcp_test(server_info)
            # return result

            tcp_test(server_info)

        elif test_type.lower() == 'http':
            # result = http_test(server_info)
            # return result

            http_test(server_info)

        else:
            raise ValueError('Valid test types are "tcp" and "http"')

    except Exception as e:
        print('Caught exception: {0}'.format(str(e)))


def send_result(test_type, server_info, recipient_email, recipient_phone=None):
    """
    send result to email and (optionally) SMS (phone)

    :param test_type: test type, eg, tcp or http
    :param server_info: server ipor hostname with port
    :param recipient_email: recipient email address
    :param recipient_phone: recipient phone number
    """

    timestamp = get_timestamp()
    test_result = server_test(test_type, server_info)

    try:
        if test_result is not False:
            subject = '{0} completed successfully:{1}, {2}'.format(
                test_type.upper(), server_info, timestamp)
            message = '{0} completed successfully: {1}, {2}'.format(
                test_type.upper(), server_info, timestamp)

        else:
            subject = 'Error: {0} test failed: {1}, {2}'.format(
                test_type.upper(), server_info, asctime())
            message = 'There was an error while executing {0} on {1}.'.format(
                test_type.upper(), server_info)

    except Exception as e:
        print(str(e))
        return False

    try:
        send_mail(subject, recipient_email, message)
        print('Successfully sent E-mail message')

    except smtplib.SMTPException as e:
        print('SMTP error: {0}'.format(str(e)))

    except RuntimeError as e:
        print('Runtime error: unable to send E-mail: {0}'.format(str(e)))

    if recipient_phone:
        try:
            print("Preparing to send SMS...")
            send(recipient_phone, message)

        except RuntimeError as e:
            print('Runtime error: unable to send SMS: {0}'.format(str(e)))

    else:
        print('No phone number supplied, skipping SMS...')

    return test_result


# for testing this script can be run at the terminal with args
if __name__ == '__main__':

    if 3 > len(argv) > 4:
        print('Incorrect number of arguments.')

    elif len(argv) == 3:
        server_test(argv[1], argv[2])

    else:
        send_result(argv[1], argv[2], argv[3])
