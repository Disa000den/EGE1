from itertools import *
cnt = 0
k = 0
for p in product('АВИОРТФ', repeat=6):
    cnt += 1
    if cnt % 2 == 0 and p[0] != 'О' and p.count('Р') == 2:
        k += 1
print(k)