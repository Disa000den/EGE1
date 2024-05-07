from itertools import *
cnt = 0
cnti = 0
for i in product('АГИЛМОРТ', repeat = 5):
    a = ''.join(i)
    cnt += 1
    if cnt % 2 != 0 and a[0] != 'Г' and a.count('И') >= 2:
        cnti += 1
print(cnti)

#с первого раза