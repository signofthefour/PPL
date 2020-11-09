def lessThan(lst, n):
    return list(filter(lambda c:  (c < n) == True , lst))

print(lessThan([1,2,3,4,5],4))