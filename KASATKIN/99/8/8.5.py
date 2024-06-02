from itertools import *
cnt = 0
for p in product('КУМА', repeat=5):
    if (p[0] == 'К' or p[0] == 'М') and (p[-1] == 'У' or p[-1] == 'А'):
        cnt += 1
print(cnt)