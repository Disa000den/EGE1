from itertools import *
cnt = 0
for p in product('АКЛОШ', repeat = 4):
    cnt += 1
    if p[0] == 'О':
        print(cnt)
