#! /usr/bin/env python3

"""tests.py: tests for server-upbot project."""

import time
import unittest
import monitor


class MonitorTest(unittest.TestCase):

    def setUp(self):
        self.tcp_url = '8.8.8.8:53'
        self.http_url = 'http://www.pdxpixel.com'

    def tearDown(self):
        self.tcp_url = ''
        self.http_url = ''

    def test_tcp_test(self):
        result = monitor.tcp_test(self.tcp_url)
        self.assertEqual(result, 'success')

    def test_http_test(self):
        result = monitor.http_test(self.http_url)
        self.assertEqual(result, 'success')

    def test_server_test(self):
        self.fail('Test not written...')

    def test_send_result(self):
        self.fail('Test not written...')


# https://docs.python.org/3/library/unittest.html
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('monitor'.upper(), 'MONITOR')
#
#     def test_isupper(self):
#         self.assertTrue('MONITOR'.isupper())
#         self.assertFalse('Monitor'.isupper())
#
#     def test_split(self):
#         s = 'Server Monitor'
#         self.assertEqual(s.split(), ['Server', 'Monitor'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

if __name__ == '__main__':
    unittest.main()
