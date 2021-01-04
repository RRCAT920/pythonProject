# -*- coding: utf-8 -*-
import threading
import time


def loop():
    print(f'{threading.current_thread().name} 启动')
    n = 0
    while n < 5:
        n += 1
        print(f'{threading.current_thread().name} >>> {n}')
        time.sleep(1)
    print(f'{threading.current_thread().name} 结束')


print(f'{threading.current_thread().name} 启动')
t = threading.Thread(target=loop, name='LoopThread')
t1 = threading.Thread(target=loop)
t.start()
t1.start()
t.join()
t1.join()
print(f'{threading.current_thread().name} 结束')