import sqlite3

class Database:
    def __init__(self, db_file = "users.db"):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_users_table()

    def create_users_table(self):
        self.cursor.execute (''' 
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL)                                            
        ''')
        self.connection.commit()

    def add_user(self, username, password):
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.connection.commit()


    def get_username(self, username):
        self.cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
        return self.cursor.fetchone()

    def get_username_password(self, username):
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()
        