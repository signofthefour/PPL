def double(x):
    return x * 2

def increase(x):
    return x + 1

def square(x):
    return x * x

def compose(x, *args):
    return compose(compose(x, *args[1:]), args[0]) if len(args) > 1 else args[0](x)

def compose2(x, *args):
    from functools import reduce
    def compose(f, g):
        return lambda x : f(g(x))

    return reduce(compose, args)(x)

from functools import reduce
lst = [1, 2, 3, 6]
print(reduce(lambda x, y: x + y, lst))


# print(compose(1, increase, square, double))
# print(compose2(1, increase, square, double))
