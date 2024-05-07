from itertools import product, permutations

def u (w, x, y, z):
    return not (x == w and not z) and (y == x and not w)
for x1, x2, x3, x4, x5, x6 in product([0,1], repeat=6):
    t= (
        (x1, x2, 0, x3, 1),
        (x4, 0, x5, 0, 1),
        (0, x6, 1, 0, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations ('wxyz', r=4):
            if all(u(**dict(zip(p,m))) == m[-1] for m in t):
                print(*p)
