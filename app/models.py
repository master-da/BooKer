import sqlite3
import pandas as pd
from flask_login import UserMixin

# This class holds info about an user
class User(UserMixin):
    id = 0
    name = ""
    email = ""
    password = ""

    def get(self, user_id):
        return UserTable().getUserFromId(user_id)

    def __repr__(self):
        return f'<User {self.name}>'

# This class interacts wiht the User table in databse        
class UserTable:
    def __init__(self):
        self.conn = sqlite3.connect('db.db')
        self.create_table()

    def create_table(self) -> bool:
        create_table = """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );"""
        try:
            self.conn.execute(create_table)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            return False
        return True

    def insert(self, name, email, password) -> bool:
        check = f"""SELECT * FROM users WHERE email = '{email}' OR name = '{name}';"""
        df = pd.read_sql_query(check, self.conn)
        if len(df) > 0:
            return False
        
        insert = f"""INSERT INTO users (name, email, password) VALUES ('{name}', '{email}', '{password}');"""
        try:
            self.conn.execute(insert)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            return False
        return True
    
    def authenticate(self, email, password) -> User:
        check = f"""SELECT * FROM users WHERE email = '{email}' AND password = '{password}';"""
        df = pd.read_sql_query(check, self.conn)
        if len(df) == 0:
            return None
        account = df.loc[0]
        
        user = User(); 
        user.id = account['id']
        user.name = account['name']
        user.email = account['email']
        user.password = account['password']

        return user
    
    def getUserFromId(self, id) -> User:
        select = f"""SELECT * FROM users where id = {id}"""
        df = pd.read_sql_query(select, self.conn)
        if len(df) == 0:
            return None
        account = df.loc[0]

        user = User(); 
        
        user.id = account['id']
        user.name = account['name']
        user.email = account['email']
        user.password = account['password']

        return user

    def select(self) -> bool:
        select = """SELECT * FROM users;"""
        df = pd.read_sql_query(select, self.conn)
        return df

    def update(self, id, name, email, password) -> bool:
        update = f"""UPDATE users SET name = '{name}', email = '{email}', password = '{password}' WHERE id = {id};"""
        try:
            self.conn.execute(update)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            return False
        return True

    def delete(self, id) -> bool:
        delete = f"""DELETE FROM users WHERE id = {id};"""
        try:
            self.conn.execute(delete)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            return False
        return True

    def close(self):
        self.conn.close()

class BookingTable:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('db.db')
        self.create_table()

    def create_table(self) -> bool:
        create_table = """CREATE TABLE IF NOT EXISTS booking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            hotel_fsq_id TEXT NOT NULL,
            check_in TEXT NOT NULL,
            check_out TEXT NOT NULL,
            adults INTEGER NOT NULL,
            children INTEGER NOT NULL,
            rooms INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );"""
        try:
            self.conn.execute(create_table)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            return False
        return True
    
    def insert(self, user_id, hotel_fsq_id, check_in, check_out, adults, children, rooms) -> bool:
        insert = f"""INSERT INTO booking (user_id, hotel_fsq_id, check_in, check_out, adults, children, rooms) VALUES ({user_id}, '{hotel_fsq_id}', '{check_in}', '{check_out}', {adults}, {children}, {rooms});"""
        try:
            self.conn.execute(insert)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            return False
        return True
    
    def select(self) -> bool:
        select = f"""SELECT * FROM booking;"""
        df = pd.read_sql_query(select, self.conn)
        return df
    
    def delete(self, id) -> bool:
        delete = f"""DELETE FROM booking WHERE id = {id};"""
        try:
            self.conn.execute(delete)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            return False
        return True
    
    def close(self):
        self.conn.close()
    