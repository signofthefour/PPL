def powGen(x):
    def pow(y):
        return x**y
    return pow

square = powGen(2)
print(square(3))