import sqlite3

def create_table_users():

    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )""")

    conn.close()
