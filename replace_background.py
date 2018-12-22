
from base import persistent
from base import primitives

with persistent.EarthBackDatabase() as db:
    db.execute('SELECT id, image, url FROM images ORDER BY score DESC')

    best_id, byte_image, url = db.fetchone()
    filename = url.split('?')[0].split('/')[-1]
    
    with open(f'imgs/{filename}') as f:
        f.write(byte_image)
    
    primitives.set_background(f'imgs/{filename}')
    

