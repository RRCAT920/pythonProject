import functools


def log(text='call'):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print(f'{text} {f.__name__}()')
            return f(*args, **kwargs)

        return wrapper

    return decorator


@log('who execute')
def now(year, month, date):
    print(f'{year}-{month}-{date}')


@log()
def fn():
    pass


# @log('em')
# def f():
#     pass
fn()

