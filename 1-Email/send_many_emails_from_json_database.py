from _init_ import *
from send_one_email import send_one_email
import pandas as pd


#осуществляет рассылку электронных писем по базе данных
def send_many_emails_from_database(database):
    if not database:
        return False
    
    try:   
        df =pd.read_json(database, orient='records')
    except ValueError:
        return False
    
    if df.shape[0]==0:
        return False
    
    if monitoring_enabled:
        from prometheus_client import start_http_server, Counter
        start_http_server(monitoring_port) #сервер prometheus
        sent_emails_counter = Counter('sent_emails_counter', 'Number of sent emails ')
        
    for row in df.itertuples():
        send_one_email(row.email,content.format(name=str(row.name),result=float(row.result)))
        #обновляем метрику для мониторинга
        if monitoring_enabled:
            sent_emails_counter.inc()
        #чтобы не было жалоб на спам - ждём определённое время
        logger.debug("waiting for {antispam_debouncer_rate} seconds".format(antispam_debouncer_rate=str(antispam_debouncer_rate)))
        time.sleep(antispam_debouncer_rate)

    return True
