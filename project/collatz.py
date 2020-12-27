# -*- coding: utf-8 -*-
"""
Collatz序列
"""


def collatz(number: int) -> int:
    if number % 2 == 1:
        return 3 * number + 1
    else:
        return number // 2


n = int(input('Enter a number:\n'))
while True:
    val = collatz(n)
    print(val)
    if val == 1:
        break
    n = val
