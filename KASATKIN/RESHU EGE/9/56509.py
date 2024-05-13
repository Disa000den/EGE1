f = open('56509.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    povt = [x for x in a if a.count(x) > 1]
    nepovt = [x for x in a if a.count(x) == 1]
    if len(povt) > 0 and len(nepovt) > 0:
        if (sum(nepovt) / len(nepovt)) > (sum(povt) / len(povt)):
            cnt += 1
print(cnt)