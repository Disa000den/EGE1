f = open('45243.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    if (a[0] + a[4])**2 > a[1] ** 2 + a[2] ** 2 + a[3] ** 2:
        cnt += 1
print(cnt)