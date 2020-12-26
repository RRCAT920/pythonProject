# -*- coding: utf-8 -*-
class MyError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise MyError(f'invalid value {s}')
    return 10 / n


# foo('0')


# reraise
def bar(s):
    try:
        foo(s)
    except ValueError as e:
        print('ValueError')
        raise


# bar('0')

try:
    10 / 0
except ZeroDivisionError as e:
    raise ValueError('0')