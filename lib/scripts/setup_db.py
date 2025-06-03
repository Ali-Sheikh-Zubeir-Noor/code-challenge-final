
import sqlite3

def setup_database():
    conn = sqlite3.connect('lib/db/app.db')
    with open("lib/db/schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()