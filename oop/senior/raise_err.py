# -*- coding: utf-8 -*-
class MyError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise MyError(f'invalid value {s}')
    return 10 / n


foo('0')
