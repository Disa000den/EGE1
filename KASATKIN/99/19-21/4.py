from functools import lru_cache


def moves(h):
    a, b = h
    if a < b:
        return (a + 1, b), (a + 3, b)
    else:
        return (a, b + 1), (a, b + 3)


@lru_cache(None)
def game(h):
    a, b = h
    if  a == b: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'


for s in range(1, 26):
    h = 10, s
    if game(h) == 'B1':
        print(s)