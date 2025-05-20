import sqlite3

def create_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("Database and table created successfully.")

if __name__ == "__main__":
    create_db()
