from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 2, b), (a * 2, b), (a, b + 2), (a, b * 2)

@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 118: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'


for s in range(1, 1000):
    h = 3, s
    if game(h) == 'B2':
        print(s)