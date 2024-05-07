from itertools import product, permutations

def u (k, l, m, n):
    return not (k <= m) and (k or n) or (l <= n)
for x1, x2, x3, x4, x5, x6, x7 in product([0,1], repeat=7):
    t= (
        (1, x1, x2, 0, 0),
        (x3, x4, x5, 1, 0),
        (0, 1, x6, x7, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations ('lkmn', r=4):
            if all(u(**dict(zip(p,m))) == m[-1] for m in t):
                print(*p)