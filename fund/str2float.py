from functools import reduce


def char2num(c):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]


def str2float(s):
    pos = s.find('.')

    integer = map(char2num, s.replace('.', ''))
    return reduce(lambda x, y: x * 10 + y, integer) / pow(10, len(s) - pos - 1)


print(str2float("123.4123"))
