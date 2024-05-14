def f(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    if d * d > n:
        return 0
    else:
        return n // d - d


n = 850001
k = 0
while k < 6:
    if f(n) != 0 and f(n) % 5 == 0:
        print(n, f(n))
        k += 1
    n += 1