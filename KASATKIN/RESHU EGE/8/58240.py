from itertools import *
cnt = 0
for i in product('012345678', repeat = 5):
    a = ''.join(i)
    if i[0] != '0' and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]) > int(i[4]):
        cnt += 1
print(cnt)

#не с первого раза