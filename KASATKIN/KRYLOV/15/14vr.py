def f(x, a):
    return (not(x % a == 0)) <= ((x % 26 == 0) <= (not(x % 169 == 0)))


for a in range(1000, 1, -1):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)