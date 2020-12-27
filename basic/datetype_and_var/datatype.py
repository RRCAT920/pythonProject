# -*- coding: utf-8 -*-
# todo: 数据类型
# 整型
assert 1 == 0x1
assert 1_000 == 1000

# 浮点型
assert 3.14 == 314e-2

# 字符串
assert 'abc' == "abc"
assert '\\t' == r'\t'
assert '''a
b''' == 'a\nb'

# 布尔值
assert True and True
assert False or True
assert not False

# 空值
assert not None
