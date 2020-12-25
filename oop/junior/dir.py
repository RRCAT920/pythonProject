# -*- coding: utf-8 -*-

def read_img(fp):
    if hasattr(fp, 'read'):
        return fp.read()
    return None
