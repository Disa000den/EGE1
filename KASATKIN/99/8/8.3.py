from itertools import *
cnt = 0
for p in product('АЛПЦЯ', repeat = 5):
    cnt += 1
    if p.count('А') <= 1 and p.count('П') == 2 and p.count('Л') == 0:
        print(cnt)