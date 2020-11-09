from functools import reduce

def flatten(lst):
    return reduce(lambda x,y: x + y, lst,[])

print(flatten([]))