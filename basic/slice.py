def my_slice(a_list, length, reverse=False):
    """切片（可以从开头或者末尾）"""
    list_sliced = []
    if not reverse:
        for i in range(length):
            list_sliced.append(a_list[i])
    else:
        for i in range(-length, 0):
            list_sliced.append(a_list[i])
    return list_sliced


print(my_slice([1, 2, 3, 4], 2))
print(my_slice([1, 2, 3, 4], 2, True))