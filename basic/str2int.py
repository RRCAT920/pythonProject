from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    itor = map(lambda ch: DIGITS[ch], s)
    return reduce(lambda x, y: 10 * x + y, itor)


print(str2int('12321321313'))