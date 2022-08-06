import unittest
import sqlite3
import pandas as pd
from create_and_populate_tables import create_and_populate_tables

class TestMethods(unittest.TestCase):
    def setUp(self):
##        print("Start test...")
        self.connect = create_and_populate_tables()

    def tearDown(self):
##        print("Stop test...")
        self.connect.close()
        
    def test_check_conn(self):
        """Проверка соединения с базой данных"""
        try:
            cur =self.connect.cursor()
            cur.execute('select * from subjects')
            self.assertTrue(True) 
            return True
        except Exception as ex:
            self.assertTrue(False) 
            return False

    def test_answer1(self):
        cur = self.connect.cursor()
        """Проверка, что 3 пользователя отсортированы по результату по убыванию"""
        df = pd.read_sql_query("""
        SELECT user.name, result.result, subjects.name
        FROM result
        JOIN user ON user.id==result.user_id
        JOIN subjects ON subjects.id==result.subject
        ORDER BY result.result DESC
        LIMIT 3;
        """, self.connect)
        self.assertTrue((df["result"][0]>=df["result"][1]) and (df["result"][1]>=df["result"][2]))

    def test_answer2(self):
        cur = self.connect.cursor()
        """Проверка, что сумма баллов пользователя больше 200 и сортировка по убыванию"""
        df = pd.read_sql_query("""
        SELECT user.name, sum(result.result) AS total_score
        FROM result
        JOIN user ON user.id==result.user_id
        GROUP BY user.id
        HAVING count(result.result)>=3 AND total_score >= 200
        ORDER BY total_score  DESC
        LIMIT 3;
        """, self.connect)
        self.assertTrue(df["total_score"][0]>=200 and df["total_score"][1]>=200 and df["total_score"][2]>=200)       
        self.assertTrue((df["total_score"][0]>=df["total_score"][1]) and (df["total_score"][1]>=df["total_score"][2]))       

if __name__ == '__main__':
    unittest.main()
