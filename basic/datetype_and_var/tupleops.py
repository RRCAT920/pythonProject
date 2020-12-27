# -*- coding: utf-8 -*-
# todo: tuple操作
# 定义
assert (1) == 1
assert isinstance((1,), tuple)

t = (1, 2, [3, 4])
t[2][0] = 5
t[2][1] = 6
assert t == (1, 2, [5, 6])

# 查
assert t[0] == 1
assert t[-1] == [5, 6]

# 长度
assert len(t) == 3

# 索引越界
try:
    a = t[len(t)]
except IndexError:
    pass

# 迭代
for val in t:
    print(val)

for index, el in enumerate(t):
    print(f't[{index}]={el}')

# 子元组
assert t[:2] == (1, 2)

# 反转
assert t[::-1] == ([5, 6], 2, 1)

# 拷贝
assert id(t[::]) != t
