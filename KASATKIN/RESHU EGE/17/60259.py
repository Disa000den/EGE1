f = open('60259.txt')
s = [int(x) for x in f]
max_elem = max([s[x] for x in range(len(s)) if s[x] % 100 == 13])
list_new = []
l = []
for i in range(len(s) - 2):
    l = sorted([s[i], s[i + 1], s[i + 2]])
    if ((len(str(l[0])) == 3 and len(str(l[1])) == 3 and len(str(l[2])) != 3)
        or (len(str(l[1])) == 3 and len(str(l[2])) == 3 and len(str(l[0])) != 3)
        or (len(str(l[2])) == 3 and len(str(l[0])) == 3 and len(str(l[1])) != 3)) \
        and (l[2] + l[1] + l[0]) <= max_elem:
        list_new.append(l[2] + l[1] + l[0])
print(len(list_new), max(list_new))
