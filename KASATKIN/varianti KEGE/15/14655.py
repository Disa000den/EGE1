def f(x, a):
    return ((x & a) != 0) <= (((x & 168) == 0) <= ((x & 69) != 0))


for a in range(100, 1, -1):
    if all(f(x, a) for x in range(1000)):
        print(a)

        #в пизду