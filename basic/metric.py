import functools
import time


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        val = fn(*args, **kwargs)
        end = time.time()
        print(f'{fn.__name__}执行了{end - start:.4f}ms')
        return val

    return wrapper
