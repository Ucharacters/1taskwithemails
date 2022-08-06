from _init_ import *
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from sys import exit
import re

#проверка адреса электронной почты через regex
def valid_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

#отправка 1 сообщения электронной почты через SMTP
def send_one_email(send_to, text):
  if not valid_email(send_to):
    logger.debug("wrong format of email="+str(send_to)+". Email is not sent.")
    return False

  if len(text)==0:
    logger.debug("no text of email. Email is not sent.")
    return False
      
  msg = MIMEMultipart(
          From=sender_email,
          Date=formatdate(localtime=True),
  )
  msg['Subject'] = subject
  msg['From'] = sender_email
  msg['To'] = receiver_email
  msg.attach(MIMEText(text, 'plain'))

  try:
      s = SMTP_SSL(smtp_server,port = 465)
      s.login(username, password) 
      logger.debug("server.login=ok")   
      try:
          s.send_message(msg)
          logger.debug("server.send_message(msg)")
      finally:
          s.quit()
          logger.debug("server.quit()")
          return True

  except Exception as E:
      logger.debug('Exception: {}'.format(str(E)))
      return False

