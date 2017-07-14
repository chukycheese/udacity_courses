def russian(a, b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1    # = times 2
        x = x >> 1    # = devide by 2
    return z

print(russian(14, 11))
