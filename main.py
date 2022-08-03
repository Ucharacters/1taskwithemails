##Задача №1
##Написать функцию, которая принимает json формата:
##[{name: str,email: str,result: float}]
##И отправляет на каждый email сообщение «Привет, Артем, твой результат: 24,5»

from _init_ import *
from send_many_emails_from_json_database import send_many_emails_from_database
from send_one_email import send_one_email

if __name__ == '__main__':
    setup_runtime_environment()
    logger.debug("Start...")
    send_many_emails_from_database(database)
    logger.debug("Stop...")

