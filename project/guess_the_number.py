# -*- coding: utf-8 -*-
"""
猜1-20中的数，只能才3次
"""
import random

secret = random.randint(1, 20)
for i in range(3):
    guess = int(input('猜一个数(1-20) >>> '))

    if guess > secret:
        print('高了')
    elif guess < secret:
        print('低了')
    else:
        print('猜中了')
        break
