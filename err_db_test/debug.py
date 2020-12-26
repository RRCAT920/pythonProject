# -*- coding: utf-8 -*-
import logging


def foo_with_print(s):
    n = int(s)
    print(f'>>> n = {n}')
    return 10 / n


# foo_with_print('0')


def foo_with_assert(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


# foo_with_assert('0')

n = int('0')
logging.info(f'n = {n}')
print(10 / n)