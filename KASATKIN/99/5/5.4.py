def f(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s


for n in range(1, 1000):
    r = f(n)
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + f((n % 3) * 3)
    r = int(r, 3)
    if r <= 138:
        print(r)