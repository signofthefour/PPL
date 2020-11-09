def lstSquare(n):
    return lstSquare(n - 1) + [n**2] if n > 1  else [1]
    
print (lstSquare(2))