import sqlite3
import pandas as pd
from create_and_populate_tables import create_and_populate_tables, DataBaseContextManager

#открываем сессию с базой данных
with DataBaseContextManager() as connect:
    print("""
    ===========================================================================
    **Необходимо написать запрос, который выдаст 3 пользователей,
    с лучшими результатами по любому из предметов и отсортировать по результату по убыванию.**
    *Пример ответа:*
    Иван, 100.0, История
    Владимир, 95.0, Математика
    Кирилл, 93.0, История
    """)

    #для удобства чтения в табличном виде
    df = pd.read_sql_query("""
    SELECT user.name, result.result, subjects.name
    FROM result
    JOIN user ON user.id==result.user_id
    JOIN subjects ON subjects.id==result.subject
    ORDER BY result.result DESC
    LIMIT 3;
    """, connect)
    print(df.head())

    print("""
    ==========================================================================
    ***** **Получить пользователей, которые сдавали по 3 предмета
    и у которых результат больше 200 по всем предметам
    и отсортировать по результату по убыванию.**
    *Пример ответа:*
    Иван, 251.0
    Владимир, 230.5
    Константин, 220.2

    """)

    #для удобства чтения в табличном виде
    df = pd.read_sql_query("""
    SELECT user.name, sum(result.result) AS total_score
    FROM result
    JOIN user ON user.id==result.user_id
    GROUP BY user.id
    HAVING count(result.result)>=3 AND total_score >= 200
    ORDER BY total_score  DESC
    LIMIT 3;
    """, connect)
    print(df.head())







