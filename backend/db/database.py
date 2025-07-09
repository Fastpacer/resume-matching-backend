
import sqlite3

conn = sqlite3.connect("job_assistant.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, contact TEXT, education TEXT, experience TEXT
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT, company TEXT, status TEXT, last_updated TEXT
)''')
conn.commit()