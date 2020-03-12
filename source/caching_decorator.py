from source.baby_functions import factorial


def cache_last(func, *size):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


cached_factorial = cache_last(factorial)
print(cached_factorial(10))
