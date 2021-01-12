# -*- coding: utf-8 -*-
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print(f'[Consumer] Consuming {n}')
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print(f'[Producer] Producing {n}')
        r = c.send(n)
        print(f'[Producer] Consumer return {r}')
    c.close()


c = consumer()
produce(c)