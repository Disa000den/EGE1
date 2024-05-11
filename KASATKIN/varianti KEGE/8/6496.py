from itertools import *
cnt = 0
for p in product('БЕРСК', repeat = 5):
    cnt += 1
for i in product('БЕРСК', repeat = 6):
    cnt += 1
for x in product('БЕРСК', repeat = 7):
    cnt += 1
print(cnt)