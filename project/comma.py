# -*- coding: utf-8 -*-
"""
逗号代码
>>> commafy(['apples', 'bananas', 'tofu', 'cats'])
'apples, bananas, tofu, and cats'
>>> commafy([1, 2, 'tofu', 3.14, True, None])
'1, 2, tofu, 3.14, True, and None'
"""
from typing import List, Any


def commafy(lst: List[Any]) -> str:
    """
    :param lst: string-like object which can transfer to a string
    """
    rs = ''
    for i in range(len(lst) - 1):
        rs += f'{lst[i]}, '
    rs += f'and {lst[len(lst) - 1]}'

    return rs


if __name__ == '__main__':
    import doctest
    doctest.testmod()