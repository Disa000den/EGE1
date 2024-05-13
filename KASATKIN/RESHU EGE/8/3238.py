from itertools import *
cnt = 0
for i in product('АКРУ', repeat = 5):
    a = ''.join(i)
    cnt += 1
    if cnt == 450:
        print(a)
        break

#С первого раза