for n in range(0, 1000):
    s = int(bin(n)[2:])
    l1 = s % 2
    last = str(l1)
    osn = str(s)
    ch = osn + last
    if ch.count('1') % 2 == 0:
        ch1 = ch + '0'
    else:
        ch1 = ch + '1'
    r = int(ch1, 2)
    if r > 105:
        print(r)
