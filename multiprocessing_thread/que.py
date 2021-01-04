# -*- coding: utf-8 -*-
import os
import random
import time
from multiprocessing import Queue, Process


def write(que):
    print(f'写进程{os.getpid()}')
    for s in 'ABC':
        print(f'将{s}写入队列')
        que.put(s)
        time.sleep(random.random())


def read(que):
    print(f'读进程{os.getpid()}')
    while True:
        val = que.get(True)
        print(f'从队列读出{val}')


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()