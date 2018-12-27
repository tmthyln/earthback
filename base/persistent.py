import sqlite3


__all__ = ['EarthBackDatabase']


class EarthBackDatabase:
    def __init__(self, file='earthback.db'):
        self.conn = sqlite3.connect(file)
        
        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS images (
        id TEXT PRIMARY KEY ON CONFLICT REPLACE,
        url TEXT,
        score INTEGER,
        description TEXT,
        short TEXT,
        path TEXT)''')
        
        self.conn.commit()
    
    def __enter__(self):
        return self.conn.cursor()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    pass

