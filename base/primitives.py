import ctypes
import os
from PIL import Image
import praw
import re
import requests

from typing import List

import config
from base import persistent


def set_background(img_filename: str):
    if not os.path.exists(img_filename):
        raise ValueError('path to new background image must exist (can be relative)')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(img_filename), 3)


reddit = praw.Reddit('earthback', user_agent='earthback app by /u/tmthyln')


def load(img_id):
    with persistent.EarthBackDatabase() as db:
        db.execute('SELECT image, url FROM images WHERE id=?', img_id)
        image, url = db.fetchone()
        
    filename = url.split('?')[0].split('/')[-1]
    
    with open(filename, 'wb') as f:
        f.write(image)
    img = Image.open(filename)
    
    os.remove(filename)
    
    return img


def fetch_and_filter(time_filter: str = 'week') -> List[str]:
    images = []
    
    with persistent.EarthBackDatabase() as db:
        for submission in reddit.subreddit(config.get_property('source')).top(time_filter, limit=500):
            # extract url info (break if no more posts)
            try:
                img_url = submission.preview['images'][0]['source']['url']
            except AttributeError:
                break
            path, query_string = img_url.split('?')
            
            # fetch data
            queries = {}
            for query in query_string.split('&'):
                bef, aft = query.split('=')
                queries[bef] = aft
            
            r = requests.get(url=path, params=queries)
            
            # extract filename
            img_filename = path.split('/')[-1]

            # extract description
            desc = re.sub('\[.*\]', '', submission.title).strip()
            
            # extract id and add to list of new images
            id_name = img_filename.split('.')[0]
            images.append(id_name)
            
            # extract image
            img = r.content
            
            # insert into database (persistent on disk)
            db.execute('INSERT INTO images VALUES (?,?,?,?,?,?)',
                       (id_name, img_url, 0, desc, '', img))
    
        db.execute('SELECT Count(id) FROM images')
        print(db.fetchone())
    
    return images


# set_background('imgs/scottish.jpg')

fetch_and_filter('year')

