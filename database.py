# database.py

import sqlite3

DB_NAME = "users.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            qualification TEXT,
            role TEXT DEFAULT 'user'
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            query TEXT,
            response TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_user_by_credentials(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result

def add_user(username, password, qualification):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, qualification) VALUES (?, ?, ?)",
                  (username, password, qualification))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def get_all_users():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users

def update_qualification(user_id, qualification):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET qualification=? WHERE id=?", (qualification, user_id))
    conn.commit()
    conn.close()

def save_chat(user_id, query, response, timestamp):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO history (user_id, query, response, timestamp) VALUES (?, ?, ?, ?)",
              (user_id, query, response, timestamp))
    conn.commit()
    conn.close()
