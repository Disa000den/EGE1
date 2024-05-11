f = open('57476.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    if len(set(a)) == 5 and (a[0] + a[-1]) * 2 <= sum(a) - (a[0] + a[-1]):
        cnt += 1
print(cnt)