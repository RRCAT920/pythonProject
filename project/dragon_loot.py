# -*- coding: utf-8 -*-
"""
龙的战利品
"""
from typing import Dict, List

from inventory import show_inventory


def add_to_inventory(inventory: Dict[str, int], items: List[str]) -> None:
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


inv = {'gold coin': 42, 'rope': 1}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inv, dragon_loot)
show_inventory(inv)
