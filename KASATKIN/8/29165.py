from itertools import *
count = 0
for p in product('РЕГИНА', repeat=5):
    if p.count('Р') == 1 and p.count('Г') == 1 and (p.count('Н') == 1 or p.count('Н') == 0):
        count += 1
print(count)