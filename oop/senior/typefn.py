# -*- coding: utf-8 -*-
def fn(self, name: str = '1'):
    return name


Hello = type('Hello', (object,), {'hello': fn})
h = Hello()

assert h.hello() == '1'
assert str(type(Hello)) == "<class 'type'>"
assert str(type(h)) == "<class '__main__.Hello'>"
