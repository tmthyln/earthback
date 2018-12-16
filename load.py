import ctypes
import os


def set_background(img_filename):
    if not os.path.exists(img_filename):
        raise ValueError('path to new background image must exist (can be relative)')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(img_filename), 3)


set_background('imgs/scottish.bmp')




