f = open('12098.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    povt = [x for x in a if x % 2 != 0]
    nepovt = [x for x in a if x % 2 == 0]
    if len(set(a)) == 2 and \
        len(povt) == 3 and len(set(povt)) == 1 and len(nepovt) == 1 and len(set(nepovt)) == 1:
        print(a)
        cnt += 1
print(cnt)