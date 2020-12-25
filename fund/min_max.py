def minmax(lst):
    if len(lst) == 0:
        return None, None
    lst.sort()
    return lst[0], lst[len(lst) - 1]


print(minmax([1, 2, 3]))