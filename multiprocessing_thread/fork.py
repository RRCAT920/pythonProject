# -*- coding: utf-8 -*-
import os

print(f'进程 ({os.getpid()}) 开始')
pid = os.fork()
if pid == 0:
    print(f'这是子进程 ({os.getpid()}), 我的父进程是 ({os.getppid()})')
else:
    print(f'这是父进程 ({os.getpid()}), 我创建了子进程 ({pid})')
