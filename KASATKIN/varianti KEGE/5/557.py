for n in range(1000):
    s = bin(n)[2:]
    a = str(s)
    if a[-1] == '0':
        a = a + '0'
    else:
        a = a + '1'
    if a.count('1') % 2 == 0:
        a = a + '01'
    else:
        a = a + '10'
    r = int(a, 2)
    if r > 144:
        print(r)
        break