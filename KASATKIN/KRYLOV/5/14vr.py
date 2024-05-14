for n in range(1, 1000):
    ch = 0
    ost = n % 4
    n = n - ost
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'
    if s.count('1') % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'
    r = int(s, 2)
    if r > 100:
        print(r)