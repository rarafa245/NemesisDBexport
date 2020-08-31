import sqlite3

def create_table_messages():

    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE messages (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                device TEXT NOT NULL,
                type INTEGER NOT NULL,
                fix INTEGER NOT NULL,
                hist INTEGER NOT NULL,
                ignition INTEGER NOT NULL,
                date TEXT NOT NULL,
                start_time TEXT NOT NULL,
                lat REAL NOT NULL,
                long REAL NOT NULL,
                speed INTEGER NOT NULL,
                angle INTEGER NOT NULL,
                direction INTEGER NOT NULL,
                time_on INTEGER NOT NULL
            )""")

    conn.close()
