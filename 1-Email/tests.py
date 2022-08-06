from _init_ import *
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from sys import exit
import re
import unittest
from send_one_email import *
from send_many_emails_from_json_database import send_many_emails_from_database
from blrns import *

class TestMethods(unittest.TestCase):
    
    def test_valid_email(self):
        """Проверка адреса электронной почты через regex"""
        self.assertTrue(valid_email("a@a.com"))
        self.assertFalse(valid_email("a@a.c"))
        
    def test_can_send_from_pandas(self):
        """Проверка возможности загрузки pandas"""
        try:
            import pandas as pd
            self.assertTrue(True) # ок, модуль pandas установлен 
        except ModuleNotFoundError:
            self.assertTrue(False) # нужно установить pandas
        
    def test_can_send_one_email(self):
        """Проверка возможности отправки 1 эмейла"""
        self.assertTrue(send_one_email("0A380E0B-0E77-41C1-A3E7-ECA5DFA242E2@laredo.ml","121"))
        self.assertFalse(send_one_email("0A380E0B-0E77-41C1-A3E7-ECA5DFA242Elaredo.ml","121"))
        self.assertFalse(send_one_email("0A380E0B-0E77-41C1-A3E7-ECA5DFA242E@laredo.ml",""))
        
    def test_can_send_many_emails_from_database(self):
        """Проверка подключения к базе данных"""
        self.assertFalse(send_many_emails_from_database(""))
        self.assertFalse(send_many_emails_from_database("invalid path to database"))
        self.assertTrue(send_many_emails_from_database(database))

    def test_mini_devsec(self):
        """Проверка падения при отправке некорректно сформированной строки"""
        for str_nasty in devsecops:
            self.assertFalse(valid_email(str(str_nasty)))    

if __name__ == '__main__':
    unittest.main()
