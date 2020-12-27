# -*- coding: utf-8 -*-
import os
import random
import time
from multiprocessing import Pool


def task(n: int) -> None:
    print(f'运行子进程{n}({os.getpid()})')
    start = time.time()
    time.sleep(random.random() * 3)
    stop = time.time()
    print(f'子进程{n}({os.getpid()}运行了{stop - start:.2f}s)')


if __name__ == '__main__':
    print(f'父进程{os.getpid()}')
    pool = Pool(4)
    for i in range(20):
        pool.apply_async(task, args=(i, ))

    print('等待子进程运行结束')
    pool.close()
    pool.join()
    print('所有子进运行结束')