f = open('59722.txt')
s = [int(x) for x in f]
max_elem = max([s[x] for x in range(len(s)) if s[x] % 100 == 17])
sum_troik = []
l = []
for i in range(len(s) - 2):
    l = sorted([s[i], s[i + 1], s[i + 2]])
    if (len(str(l[0])) == 3 and len(str(l[1])) != 3 and len(str(l[2])) != 3)\
        or (len(str(l[1])) == 3 and len(str(l[2])) != 3 and len(str(l[0])) != 3) \
        or (len(str(l[2])) == 3 and len(str(l[0])) != 3 and len(str(l[1])) != 3)\
        and (l[1] + l[2] + l[0]) < max_elem:
        print(l[0], l[1], l[2])
        sum_troik.append(l[0] + l[1] + l[2])
print(len(sum_troik))

#nepravilnoe govno