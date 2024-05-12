from itertools import *
cnt = 0
for p in product('ИНФА', repeat=6):
    if p.count('Ф') == 2:
        cnt += 1
        print(p)
print(cnt)