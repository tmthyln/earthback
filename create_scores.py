import matplotlib.pyplot as plt
from PIL import Image

from base import persistent


if __name__ == '__main__':
    with persistent.EarthBackDatabase() as db:
        db.execute('SELECT id, path FROM images WHERE score=-1')
        
        for id_name, path in db.fetchall():
            print(f'LONG:  {desc}')
            
            img = Image.open(path)
            plt.show(img)
            
            score = input('Score: ')
            if score == 'q':
                break
            
            db.execute('UPDATE images SET score=? WHERE id=?', (score, id_name))

