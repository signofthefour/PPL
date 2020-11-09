def dist(lst, n):
    return [(lst[0], n)] + dist(lst[1:], n)  if len(lst) > 0 else []

print(dist([1,2,3],4))