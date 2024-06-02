from itertools import *
cnt = 0
for p in product('КАТЕР', repeat = 4):
    if p.count('Р') >= 2:
        cnt += 1
print(cnt)