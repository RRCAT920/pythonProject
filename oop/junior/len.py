# -*- coding: utf-8 -*-

class MyObject(object):
    def __len__(self):
        return 100


o = MyObject()
print(len(o))
