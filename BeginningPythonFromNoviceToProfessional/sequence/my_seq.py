# -*- coding: utf-8 -*-
def _check_index(key: int) -> None:
    # 语法检查+运行检查
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    """
    等差数列
    首项：a0
    公差：d
    >>> s = ArithmeticSequence(1, 2)
    >>> s[4]
    9
    >>> s[4] = 2
    >>> s[4]
    2
    >>> s[5]
    11
    """

    def __init__(self, a0: int = 0, d: int = 1):
        self.a0 = a0
        self.d = d
        self.container = {}

    def __getitem__(self, key: int):
        _check_index(key)
        try:
            return self.container[key]
        except KeyError:
            return self.a0 + key * self.d

    def __setitem__(self, key: int, value: int):
        _check_index(key)
        self.container[key] = value


if __name__ == '__main__':
    import doctest

    doctest.testmod()
