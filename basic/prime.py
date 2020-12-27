def odds():
    n = 1
    while True:
        n += 2
        yield n


def primes():
    """通过埃氏筛选法求所有素数"""
    yield 2
    odd_itor = odds()
    while True:
        n = next(odd_itor)
        yield n
        odd_itor = filter(lambda x: x % n > 0, odd_itor)


for n in primes():
    if n > 1000:
        break
    print(n)