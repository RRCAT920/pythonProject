# -*- coding: utf-8 -*-
# todo: list操作
# 定义
numbers = [1, 2, 3]

# 增
numbers.append(4)
assert numbers == [1, 2, 3, 4]

# 删
assert numbers.pop() == 4
assert numbers == [1, 2, 3]

assert numbers.pop(0) == 1
assert numbers == [2, 3]

# 改
numbers[0] = 1
assert numbers == [1, 3]

# 查
assert numbers[0] == 1
assert numbers[-1] == 3

# 插
numbers.insert(1, 2)
assert numbers == [1, 2, 3]

# 长度
assert len(numbers) == 3

# 索引越界
try:
    a = numbers[len(numbers)]
except IndexError:
    pass

# 子列表
assert numbers[:1] == [1]
assert numbers[-1:] == [3]

# 反转
assert numbers[::-1] == [3, 2, 1]

# 拷贝
assert id(numbers[::]) != id(numbers)

# 迭代
i = 1
for number in numbers:
    assert number == i
    i += 1

for index, val in enumerate(numbers):
    print(f'numbers[{index}]={val}')