f = open('52180.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    chet = [x for x in a if x % 2 == 0]
    nechet = [x for x in a if x % 2 != 0]
    if len(set(a)) == len(a) and len(chet) > len(nechet) and sum(chet) < sum(nechet):
        cnt += 1
print(cnt)