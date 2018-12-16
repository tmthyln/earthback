import ctypes
import os


def set_as_background(img_filename):
    if not os.path.exists(img_filename):
        raise ValueError('file to new background image must exist (can be relative path)')
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(img_filename), 0)


set_as_background("imgs/scottish.bmp")
