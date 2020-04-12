from functools import reduce


def max_from_list(li):
    return ''.join(sorted(reduce(lambda x, y: str(x) + str(y), li), reverse=True))


print(max_from_list([4, 2, 3]))
