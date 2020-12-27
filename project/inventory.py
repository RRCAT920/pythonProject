# -*- coding: utf-8 -*-
"""
玩家背包清单

Example

>>> show_inventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})
Inventory:
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
Total number of items: 62
"""
from typing import Dict


def show_inventory(inv: Dict[str, int]) -> None:
    print('Inventory:')
    total = 0
    for k, v in inv.items():
        print(f'{v} {k}')
        total += v
    print(f'Total number of items: {total}')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
