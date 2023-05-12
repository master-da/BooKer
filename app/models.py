import sqlite3
import pandas as pd

class UserTable:
    def __init__(self):
        self.conn = sqlite3.connect('db.db')
        self.create_table()

    def create_table(self):
        create_table = """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );"""
        self.conn.execute(create_table)
        self.conn.commit()

    def insert(self, name, email, password):
        insert = f"""INSERT INTO users (name, email, password) VALUES (
            '{name}', '{email}', '{password}'
        );"""
        self.conn.execute(insert)
        self.conn.commit()

    def select(self):
        select = """SELECT * FROM users;"""
        df = pd.read_sql_query(select, self.conn)
        return df

    def update(self, id, name, email, password):
        update = f"""UPDATE users SET name = '{name}', email = '{email}', password = '{password}' WHERE id = {id};"""
        self.conn.execute(update)
        self.conn.commit()

    def delete(self, id):
        delete = f"""DELETE FROM users WHERE id = {id};"""
        self.conn.execute(delete)
        self.conn.commit()

    def close(self):
        self.conn.close()

