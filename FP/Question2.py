from functools import reduce

def flatten(lsts):
    return [item for lst in lsts for item in lst]

def flatten1(lsts):
    return list(lsts[0] + flatten1(lsts[1:]) if len(lsts) > 0 else [])

def flatten2(lsts):
    return reduce(lambda x,y: x + y, lsts)

stm = [[1,2,3],['a','b','c'],[1.1,2.1,3.1]]
print(flatten(stm))
print(flatten1(stm))
print(flatten2(stm))
