f = open('59687.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    if len(a) - len(set(a)) == 2:
        povt = [x for x in a if a.count(x) == 3]
        if (sum(a) - sum(povt)) / 4 <= sum(povt) / 3:
            cnt += 1
print(cnt)
