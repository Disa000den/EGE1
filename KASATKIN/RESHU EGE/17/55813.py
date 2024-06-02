f = open('55813.txt')
a = []
for s in f:
    a.append(abs(int(s)))
mn = 100000
for k in range(len(a)):
    if len(str(a[k])) == 3 and a[k] % 10 == 5:
        mn = min(mn, a[k])
sum_pari = []
for i in range(len(a) - 1):
    if (100 <= a[i] < 1000 and (a[i + 1] < 100 or a[i + 1] >= 1000)) or (100 <= a[i + 1] < 1000 and (a[i + 1] < 100 or a[i] >= 1000)):
        if (a[i] + a[i + 1]) % mn == 0:
            sum_pari.append(a[i] + a[i + 1])
print(len(sum_pari), min(sum_pari))