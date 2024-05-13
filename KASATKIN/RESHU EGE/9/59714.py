f = open('59714.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    povt = [x for x in a if a.count(x) == 2]
    if len(povt) == 4 and len(set(a)) == 5:
        if (sum(a) - sum(povt)) / 3 > sum(povt) / 4:
            cnt += 1
print(cnt)