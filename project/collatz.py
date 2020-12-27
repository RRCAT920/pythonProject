# -*- coding: utf-8 -*-
"""
Collatz序列
"""


def collatz(number: int) -> int:
    if number % 2 == 1:
        return 3 * number + 1
    else:
        return number // 2


try:
    n = int(input('Enter a number:\n'))
    if n < 0:
        raise Exception("Don't input negative number")
    while True:
        n = collatz(n)
        print(n)
        if n == 1:
            break
except ValueError:
    print('Please input an integer')
except Exception as e:
    print(e)