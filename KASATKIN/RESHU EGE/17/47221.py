f = open('47221.txt')
a = []
for s in f:
    a.append(abs(int(s)))
sum_pari = []
mx = max([x for x in a if x % 10 == 3])
for i in range(len(a) - 1):
    if (abs(a[i] % 10) == 3 and abs(a[i + 1] % 10) != 3) or (abs(a[i] % 10) != 3 and abs(a[i + 1] % 10) == 3):
        if ((a[i] ** 2) + (a[i + 1] ** 2)) > (mx ** 2):
            sum_pari.append((a[i] ** 2) + (a[i + 1] ** 2))
print(len(sum_pari), max(sum_pari))