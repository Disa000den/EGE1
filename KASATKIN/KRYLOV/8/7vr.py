from itertools import *
cnt = 0
for p in product('КНОРСЯ', repeat=6):
    cnt += 1
    if p.count('К') <= 3 and p.count('Я') == 2:
        print(cnt)
        break