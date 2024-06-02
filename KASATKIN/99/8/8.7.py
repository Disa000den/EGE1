from itertools import *
cnt = 0
for p in product('МАРТ', repeat = 6):
    if p.count('Р') == 2:
        cnt += 1
print(cnt)