from functools import lru_cache


def moves(h):
    a = h
    return (a // 4), (a - 5)


@lru_cache(None)
def game(h):
    a = h
    if a <= 15: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'


for s in range(16, 581):
    h = s
    if game(h) == 'B2':
        print(s)