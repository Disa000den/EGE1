from functools import lru_cache
from sys import *

setrecursionlimit(10000)
@lru_cache(None)
def moves(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)

setrecursionlimit(10000)
@lru_cache(None)
def game(h):
    a, b = h
    if 70 <= a * b <= 110: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'S1'
    if all(game(m) == 'S1' for m in moves(h)): return 'D1'
    if any(game(m) == 'D1' for m in moves(h)): return 'S2'
    if all(game(m) == 'S1' or game(m) == 'S2' for m in moves(h)): return 'D2'


for s in range(1, 66):
    h = 5, s
    if game(h) == 'S1':
        print(s, game(h))
#уёбищная хуйня