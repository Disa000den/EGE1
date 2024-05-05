from itertools import product, permutations

def u (x, y, w, z):
    return ((z <= x) == (w <= y) or (x and w))

for x1, x2, x3, x4, x5, x6 in product ([0,1], repeat=6):
     t= (
       (x1, x2, x3, 1, 0),
       (x4, x5, 1, 1, 0),
       (x6, 1, 1, 1, 0)
      )
     if len(t) == len(set(t)):
         for p in permutations('xywz', r=4):
             if all (u(**dict(zip(p, m))) == m[-1] for m in t):
                 print(*p)