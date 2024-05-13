from itertools import *
cnt = 0
for i in product('КОР', repeat = 5):
    a = ''.join(i)
    cnt += 1
    if cnt == 238:
        print(a)
        break

#с первого раза
