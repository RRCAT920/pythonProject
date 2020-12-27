# -*- coding: utf-8 -*-
# todo: 字符串编码

assert ord('A') == 65
assert chr(65) == 'A'

assert 'abc'.encode('ascii') == b'abc'
assert b'abc'.decode('ascii') == 'abc'

assert len('中文str') == 5