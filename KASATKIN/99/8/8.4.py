from itertools import *
cnt = 0
for p in product('ЕКМОПРТЬЮ', repeat = 5):
    cnt += 1
    if p[0] != 'Е' and p.count('К') == 2:
        print(cnt, p)