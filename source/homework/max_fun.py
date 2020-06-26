from functools import cmp_to_key
from itertools import permutations


def stupid_max(input_list):
    return max(map(lambda x: ''.join(map(lambda y: str(y), x)), permutations(input_list)))


def fine_max(input_list):
    return sorted(input_list, key=cmp_to_key(compare))


def compare(x, y):
    if f"{x}{y}" > f"{y}{x}":
        return -1
    elif f"{x}{y}" < f"{y}{x}":
        return 1


def recursive_max(input_list):
    if not input_list:
        return []
    first, *tail = input_list
    return recursive_max([a for a in tail if f"{a}{first}" > f"{first}{a}"]) + [
        first] + recursive_max([a for a in tail if f"{a}{first}" < f"{first}{a}"])


print(fine_max([5299, 52]))
print(recursive_max([1234, 9]))
print(recursive_max([98, 9, 34]))
