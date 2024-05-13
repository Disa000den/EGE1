from itertools import *
cnt = 0
for i in product('012345678', repeat = 5):
    a = ''.join(i)
    if a.count('3') == 2 and a[0] != '0':
        if '12' in a or '32' in a or '52' in a or '72' in a or '21' in a or '23' in a or '25' in a or '27' in a:
            continue
        else:
            cnt += 1
print(cnt)

#с первого раза