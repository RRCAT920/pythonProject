# -*- coding: utf-8 -*-
import threading

balance = 0
mutex = threading.Lock()


def change(amount: int) -> None:
    global balance
    balance += amount
    balance -= amount


def run(amount: int) -> None:
    for i in range(2_000_000):
        with mutex:
            change(amount)


t1 = threading.Thread(target=run, args=(5,))
t2 = threading.Thread(target=run, args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
