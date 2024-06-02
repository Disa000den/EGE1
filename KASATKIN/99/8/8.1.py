from itertools import *
cnt = 0
for p in product('КОР', repeat=5):
    cnt += 1
    if cnt == 182:
        print(p)