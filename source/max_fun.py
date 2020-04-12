from functools import reduce


def max_from_list(li):
    return int(reduce(lambda x, y: str(x) + str(y), li))


print(max_from_list([1, 2, 3]))
