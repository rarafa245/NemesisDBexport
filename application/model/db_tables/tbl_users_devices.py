import sqlite3

def create_table_users_devices():

    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE users_devices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device TEXT NOT NULL,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )""")

    conn.close()
