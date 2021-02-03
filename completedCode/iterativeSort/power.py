def raise_power(a, b):
    if b == 1:
        return a
    else:
        return(a * raise_power(a, b - 1))

print(raise_power(4, 2))

print(raise_power(2, 1))