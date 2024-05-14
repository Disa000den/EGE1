from itertools import *
cnt = 0
k = 0
for p in product('АГЕИЛНРТ', repeat=5):
    k += 1
    if k % 2 != 0 and p[0] != 'Т' and (p.count('Н') == 1 or p.count('Н') == 2):
        cnt += 1
print(cnt)