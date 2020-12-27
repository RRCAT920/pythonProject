def triangles():
    lst = [1]
    while True:
        yield lst
        lst = [1] + [lst[i] + lst[i + 1] for i in range(len(lst) - 1)] + [1]


def triangles2():
    L = [1]
    while True:
        yield L
        L = [1, *[L[i] + L[i + 1] for i in range(len(L) - 1)], 1]


