def cache_last(func, *size):
    cache_last.cache = dict()

    def memoized_func(*args):
        if args in cache_last.cache:
            return cache_last.cache[args]
        result = func(*args)
        cache_last.cache[args] = result
        return result

    return memoized_func


# cached_factorial = cache_last(factorial)
# print(cached_factorial(10))

def return_text(txt):
    return txt


cached_txt = cache_last(return_text)

print(cached_txt('some text'))

print(cache_last.cache)
