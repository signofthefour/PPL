from functools import reduce

lst = [[1,2,3],['a','b','c'],[1.1,2.2,3.3]]

def flatten_a(plst):
    newlst = []
    for i in plst:
        for n in i:
            newlst.append(n)
    return newlst
    
def flatten_b(plst):
    if plst:
        return plst[0] + flatten_b(plst[1:])
    else:
        return []

def flatten_c(plst):
    return reduce(lambda l1,l2: l1 + l2, plst)

print(flatten_a(lst))
print(flatten_b(lst))
print(flatten_c(lst))