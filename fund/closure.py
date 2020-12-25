def my_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def lazy_sum(*numbers):
    def sum_helper():
        ax = 0
        for n in numbers:
            ax += n
        return ax

    return sum_helper


f1 = lazy_sum(1, 2, 3)
f2 = lazy_sum(1, 2, 3)
assert f1 != f2
