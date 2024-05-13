f = open('33103.txt')
cnt = 0
for s in f:
    a = [x for x in s]
    if a.count('A') > a.count('E'):
        cnt += 1
print(cnt)