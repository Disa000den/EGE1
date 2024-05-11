f = open('4589.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    if a[-1] < a[0] + a[1] + a[2]:
        if a[0] + a[1] == a[2] + a[3] or a[0] + a[2] == a[1] + a[3] or a[0] + a[3] == a[1] + a[2]:
            cnt += 1
print(cnt)