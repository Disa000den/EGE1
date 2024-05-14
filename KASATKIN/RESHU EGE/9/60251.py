f = open('60251.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    povt = [x for x in a if a.count(x) == 2]
    if len(povt) == 4:
        if sum(povt) / 4 < sum(a) / 7:
            cnt += 1
print(cnt)