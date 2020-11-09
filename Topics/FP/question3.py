from functools import reduce


lst = [1,55,6,2]
n = 50

def question3_a(n, lst):
    return [ a for a in lst if a < n]

def question3_b(n, lst):
    if lst:
        return ([lst[0]] if lst[0] < n else []) + question3_b(n, lst[1:])
    else: 
        return []

def question3_c(n, lst):
    return reduce(lambda x,y: x + [y] if [y] < n else x, lst,[])

print(question3_a(n, lst))
print(question3_b(n, lst))
print(question3_c(n, lst)) 