# -*- coding: utf-8 -*-
from multiprocessing import Process
import os


def task(name: str) -> None:
    print(f'子进程({os.getpid()})跑了一个{name}')


if __name__ == '__main__':
    print(f'父进程({os.getpid()})')
    child = Process(target=task, args=('测试', ))
    print('子进程开始')
    child.start()
    child.join()  # 等待子进程结束
    print('子进程终止')
