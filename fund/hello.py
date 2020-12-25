#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = "huzihao"

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, World!')
    elif len(args) == 2:
        print(f'Hello, {args[1]}')
    else:
        print("Too many arguments!")


if __name__ == '__main__':
    test()


def _say_hello(name):
    return f"Hello, {name}"


def _say_hi(name):
    return f'Hi, {name}'


def greeting(name):
    if len(name) > 3:
        return _say_hi(name)
    else:
        return _say_hello(name)