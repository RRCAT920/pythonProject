# -*- coding: utf-8 -*-
"""
GIL
"""

import threading
import multiprocessing


def loop() -> None:
    x = 0
    while True:
        x ^= 1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
