def f(n):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'
    if s.count('1') % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'
    return int(s, 2)


for n in range(0, 100):
    if f(n) > 85:
        print(n)
        break
