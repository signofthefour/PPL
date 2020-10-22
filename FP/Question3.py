def lessThan1(n, lst):
    return [x for x in lst if x < n]

def lessThan2(n, lst):
    return ([lst[0]] if lst[0] < n else []) + lessThan2(n, lst[1:]) if len(lst) > 0 else []

def lessThan3(n, lst):
    return list(filter(lambda x : x < n, lst))

def lessThan4(n, lst):
    from functools import reduce
    return list(reduce(lambda a,b: a + [b] if b < n else a, lst, []))

# print(lessThan1(50, [1,2,50]))
# print(lessThan2(50, [1, 2, 50]))
# print(lessThan3(50, [1, 2, 50]))
print(lessThan4(50, [1, 2, 50]))
# a = 2 + [1]