f = open('37336.txt')
a = []
for s in f:
    a.append(int(s))
sum_pari = []
for i in range(len(a) - 1):
    if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
        sum_pari.append(a[i] + a[i + 1])
print(len(sum_pari), max(sum_pari))