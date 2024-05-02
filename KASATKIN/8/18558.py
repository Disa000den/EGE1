from itertools import product
count = 0
alphabet = 'ИВАН'
for p in product(alphabet, repeat = 5):
    if p.count('И') >= 1:
        count += 1
        print(p)
print(count)
