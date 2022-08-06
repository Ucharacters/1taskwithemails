import sqlite3

#вспомогательный класс для автоматического закрытия базы данных
class DataBaseContextManager:
    def __init__(self):
        self.db = create_and_populate_tables()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


#создаём и заполняем таблицы
def create_and_populate_tables():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    
    cur.executescript("""PRAGMA foreign_keys=ON;
       CREATE TABLE IF NOT EXISTS user(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       email TEXT);
       CREATE TABLE IF NOT EXISTS subjects(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT);
       CREATE TABLE result(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        result FLOAT,
        user_id INTEGER,
        subject INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
        FOREIGN KEY (subject) references subjects(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
    );
    """)
    conn.commit()
    #заполняем таблицы данными
    rows = [("русский язык",),("литература",),("математика",),("иностранный язык",),("история",)]
    conn.executemany('INSERT INTO subjects(name) VALUES(?)', rows)
    conn.commit()
    cur.executescript("""INSERT INTO user(name, email) VALUES
        ('Иван', '1@1.com'),
        ('Владимир', '2@1.com'),
        ('Кирилл', '3@1.com'),
        ('Константин', '4@1.com'),
        ('Пётр', '5@1.com');
    """)
    conn.commit()

    cur.executescript("""INSERT INTO result(user_id, result, subject) VALUES
        (4, 95.0, 1),
        (4, 75.0, 2),
        (4, 85.0, 3),
        (4, 65.0, 4),

        (1, 44.0, 4),
        (1, 34.0, 2),
        (1, 24.0, 3),
        (1, 14.0, 1),

        (2, 93.0, 2),
        (2, 73.0, 3),
        (2, 83.0, 1),

        (5, 97.0, 2),
        (5, 77.0, 3),
        (5, 87.0, 1),
        (5, 77.0, 5),
        (5, 87.0, 4),

        (3, 82.0, 3),
        (3, 62.0, 2);
    """)
    conn.commit()
    return conn
