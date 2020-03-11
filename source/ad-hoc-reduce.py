def ad_hoc_reduce(function, sequence, accumulator):
    def inner_reduce(func, seq, acc):
        [head, *tail] = seq
        inner_reduce.acc = func(acc, head)
        if tail:
            inner_reduce(func, tail, inner_reduce.acc)
        return inner_reduce.acc

    return inner_reduce(function, sequence, accumulator)


print(ad_hoc_reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5], 0))
