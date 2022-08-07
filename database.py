import sqlite3

class DataBase:
    def __init__(self, database):
        self.db = sqlite3.connect(database)
        self.sql = self.db.cursor()
        self.sql.execute("""CREATE TABLE IF NOT EXISTS films (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            image_url TEXT,
            abstract TEXT
        )""")
        self.db.commit()

    def save(self, article_lst):
        for i in range(len(article_lst)):
            self.sql.execute(f"INSERT INTO films (title, image_url, abstract) VALUES ('{article_lst[i].title}', '{article_lst[i].image_url}', '{article_lst[i].abstract}')")
            self.db.commit()

    def get(self, film_id):
        res = self.sql.execute(f"SELECT title, image_url, abstract  FROM films WHERE id = '{film_id}'").fetchone()
        if res is None:
            return None
        self.db.commit()
        return res