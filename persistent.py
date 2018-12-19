import sqlite3

conn = sqlite3.connect('earthback.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS images (
             id TEXT PRIMARY KEY ON CONFLICT REPLACE,
             url TEXT,
             score INTEGER,
             description TEXT,
             short TEXT)''')
