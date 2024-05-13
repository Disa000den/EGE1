from functools import lru_cache


def moves(h):
    a = h
    return (a + 1), (a * 2)

@lru_cache(None)
def game(h):
    a = h
    if a >= 161: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)): return 'B2'


for s in range(1, 1000):
    h = s
    if game(h) == 'B2':
        print(s, game(h))