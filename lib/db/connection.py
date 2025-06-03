import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "app.db")

conn = sqlite3.connect(DB_PATH)  # module-level connection variable

conn.row_factory = sqlite3.Row

def get_connection():
    return conn
