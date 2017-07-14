def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

# naive(a, b) calculates a * b
for i in range(1, 10):
    for j in range(1, 10):
        print(naive(i, j))
