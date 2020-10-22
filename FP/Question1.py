
def double1(lst):
    return [x * 2 for x in lst]

def double2(lst):
    return [lst[0] * 2] + double2(lst[1:]) if len(lst) > 0 else []

def multiply(x, y):
    return x * y

def double3(lst, func):
    return list(map(lambda x : func(x,2), lst))

# def double1(lst):
#     return list(map(lambda x: x*2, lst))


print(double1([1,2,3]))
print(double2([1,2,3]))
print(double3([1,2,3], multiply))
