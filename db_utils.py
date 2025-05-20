import sqlite3

DB_NAME = 'finance.db'

def insert_transaction(date, amount, category, type_, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (date, amount, category, type, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, amount, category, type_, description))
    conn.commit()
    conn.close()

def fetch_all_transactions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    rows = cursor.fetchall()
    conn.close()
    return rows
