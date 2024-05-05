from itertools import product, permutations

def u (x, y, w, z):
    return (not (x) and (z <= y) and (not w)) or ((z == w) and ((x or y) <= w))
for x1, x2, x3, x4 in product ([0,1], repeat = 4):
    t= (
      (1, 0, 0, 0, 1),
      (x1, 1, 0, x2, 1),
      (1, 0, x3, x4, 1)
    )
    if len(t) == len(set(t)):
       for p in permutations ('xywz', r=4):
          if all(u(**dict(zip(p, m))) == m[-1] for m in t):
               print(*p)