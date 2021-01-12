# -*- coding: utf-8 -*-
class CounterList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.cnt = 0

    def __getitem__(self, index: int):
        self.cnt += 1
        return super().__getitem__(index)


if __name__ == '__main__':
    clist = CounterList(1, 2, 3, 4)
    assert clist[0] + clist[3]
    assert 2 == clist.cnt
