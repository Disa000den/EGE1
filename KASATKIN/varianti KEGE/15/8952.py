def f(x, a):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & a != 0)


for a in range(1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)
