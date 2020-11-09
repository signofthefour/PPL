def powGen(x):
    def pow(y):
        return y**x
    return pow

square = powGen(2)
print(square(4))