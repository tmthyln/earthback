import ctypes
import os
import praw
import requests

from typing import List

import config


def set_background(img_filename: str):
    if not os.path.exists(img_filename):
        raise ValueError('path to new background image must exist (can be relative)')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(img_filename), 3)


reddit = praw.Reddit('earthback', user_agent='earthback app by /u/tmthyln')


def fetch_and_filter(time_filter: str = 'week') -> List[str]:
    images = []
    
    for submission in reddit.subreddit(config.get_property('source')).top(time_filter):
        # extract url info
        img_url = submission.preview['images'][0]['source']['url']
        path, query_string = img_url.split('?')
        
        # create HTTP GET parameters
        queries = {}
        for query in query_string.split('&'):
            bef, aft = query.split('=')
            queries[bef] = aft
        
        # fetch image
        r = requests.get(url=path, params=queries)
        
        # extract filename and add to list
        img_filename = path.split("/")[-1]
        images.append(img_filename)
        
        # save image to disk
        with open(f'imgs/{img_filename}', 'wb') as f:
            f.write(r.content)
        
    return images


# set_background('imgs/scottish.jpg')

fetch_and_filter()

