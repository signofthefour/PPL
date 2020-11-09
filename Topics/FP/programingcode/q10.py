from functools import reduce

def compose(*g):
    def func(args):
        return reduce(lambda x, y: y(x), reversed(g), args)
    return func 