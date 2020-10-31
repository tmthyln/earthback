
from base import persistent
from base import primitives

with persistent.EarthBackDatabase() as db:
    db.execute('SELECT id, path FROM images')
    print('executed on database')
    best_id, best_path = db.fetchone()
    print('fetched data from database')
    primitives.set_background(best_path)
    

