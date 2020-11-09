lst1 = [1,2,3,5]

def double_a(a):
    newL =[]
    for n in a:
        newL.append(n * 2)
    return newL

def double_b(b):
    if b:
        return [b[0] * 2] + double_c(b[1:])
    else:
        return []

def double_c(c):
    return list(map(lambda x: x*2,c))


print(double_a(lst1))
print(double_b(lst1))
print(double_c(lst1))