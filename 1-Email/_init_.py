from loguru import logger
import time
import os
import getpass


smtp_server = "smtp.yandex.ru"
sender_email = "0A380E0B-0E77-41C1-A3E7-ECA5DFA242E2@laredo.ml"
username = sender_email
receiver_email = "0A380E0B-0E77-41C1-A3E7-ECA5DFA242E2@laredo.ml"
port = 465  # для SSL подключения
subject = 'Sent from Python 3.x'
content = "Привет, {name}, твой результат: {result:.1f}"
password = ""
antispam_debouncer_rate=int(round(86400/3000)) #яндекс не разрешает отправлять более 3000 сообщений в сутки
database='name_email_grade.json'
logs_storage_file="file_{time}.log"
monitoring_enabled=True
monitoring_port=8000

def setup_runtime_environment():
    """Настраивает логирование и получает пароль безопасным образом"""
    logger.add(logs_storage_file, retention="10 days")  
    global password   

    try:
        with open("password.txt","r") as file_handler:
            password = file_handler.read()
            file_handler.close()
    except FileNotFoundError:
        print('Пароль Вам должен был выслать администратор.(если у Вас нет пароля - нажмите Ctrl+C)')
        entered_password=getpass.getpass(prompt='Введите пароль :' )
        with open("password.txt","w") as file_handler:
            file_handler.write(str(entered_password))
            file_handler.close()
