f = open('45251.txt')
a = []
for s in f:
    a.append(int(s))
sum_pari = []
me = min([x for x in a if x % 21 == 0])
for i in range(len(a) - 1):
    if a[i] % me == 0 or a[i + 1] % me == 0:
        sum_pari.append(a[i] + a[i + 1])
print(len(sum_pari), max(sum_pari))