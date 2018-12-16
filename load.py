import ctypes
import os
import praw
import requests

import config


def set_background(img_filename):
    if not os.path.exists(img_filename):
        raise ValueError('path to new background image must exist (can be relative)')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(img_filename), 3)


reddit = praw.Reddit('earthback', user_agent='earthback app by /u/tmthyln')


def fetch_and_filter(time_filter='week'):
    for submission in reddit.subreddit(config.get_property('source')).top(time_filter):
        img_url = submission.preview['images'][0]['source']['url']
        path, query_string = img_url.split('?')[-1]
        
        queries = {}
        for query in query_string.split('&'):
            bef, aft = query.split('=')
            queries[bef] = aft
        
        r = requests.get(url=path, params=queries)

        with open('test.jpg', 'wb') as f:
            f.write(r.content)


set_background('imgs/scottish.jpg')

fetch_and_filter()

