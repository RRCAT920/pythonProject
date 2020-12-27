import math


def __abs(number):
    if not isinstance(number, (float, int)):
        raise TypeError('bad operand type')
    if number >= 0:
        return number
    else:
        return -number


# __abs('A')


def quadratic(a, b, c):
    delta = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    return x1, x2


print(quadratic(1, -1, -2))


def pow(x, n=2):
    s = 1
    for i in range(n):
        s *= x
    return s
