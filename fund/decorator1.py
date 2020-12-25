import functools


def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print(f'call {f.__name__}()')
        return f(*args, **kw)

    return wrapper


@log
def now(year, month, date):
    print(f'{year}-{month}-{date}')


# now = log(now)
now(2020, 12, 2)
print(now.__name__)
