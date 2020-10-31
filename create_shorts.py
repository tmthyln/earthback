from base import persistent

if __name__ == '__main__':
    with persistent.EarthBackDatabase() as db:
        db.execute('SELECT id, description FROM images WHERE short=""')
        
        for id_name, desc in db.fetchall():
            print(f'LONG:  {desc}')
            short = input('SHORT: ')
            
            if short == 'q':
                break
            
            db.execute('UPDATE images SET short=? WHERE id=?', (short, id_name))
