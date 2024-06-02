from itertools import *
cnt = 0
for p in product('ABCX', repeat=5):
    if (p[-1] == 'X' and p.count('X') == 1) or p.count('X') == 0:
        cnt += 1
print(cnt)