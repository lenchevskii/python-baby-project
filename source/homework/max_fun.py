from functools import cmp_to_key
from itertools import permutations


def stupid_max(input_list):
    return max(map(lambda x: ''.join(map(lambda y: str(y), x)), permutations(input_list)))


def fine_max(input_list):
    return sorted(input_list, key=cmp_to_key(compare))


def compare(x, y):
    if "{}{}".format(x, y) > "{}{}".format(y, x):
        return -1
    elif "{}{}".format(x, y) < "{}{}".format(y, x):
        return 1
    else:
        return 0


def max_fine_recursion(input_list):
    if not input_list:
        return []
    first, *tail = input_list
    return max_fine_recursion([a for a in tail if "{}{}".format(a, first) > "{}{}".format(first, a)]) + [
        first] + max_fine_recursion([a for a in tail if "{}{}".format(a, first) < "{}{}".format(first, a)])


print(max_fine_recursion([5299, 52]))
print(max_fine_recursion([1234, 9]))
print(max_fine_recursion([98, 9, 34]))
