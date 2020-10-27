def double(x):
    return x * 2

def increase(x):
    return x + 1

def square(x):
    return x * x

# def compose(x, *args):
#     return compose(compose(x, *args[1:]), args[0]) if len(args) > 1 else args[0](x)

def compose2(x, *args):
    from functools import reduce
    def compose(f, g):
        return lambda x : f(g(x))

    return reduce(compose, args)(x)

def compose(*funcs):
    def compose2func(f,g):
        return lambda x: f(g(x))
    from functools import reduce
    return reduce(lambda x,y: compose2func(x, y), funcs, lambda x: x)


f = compose(increase, square, double) # 2*2 = 4, 4**2 = 16, 16 inc = 17
print(f(2))
# print(compose(1, increase, square, double))
# print(compose2(1, increase, square, double))
