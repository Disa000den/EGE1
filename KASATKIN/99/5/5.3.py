for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = s + '0'
        s = s.replace(s[0], '1')
        s = s.replace(s[1], '0')
    else:
        s = s + '1'
        s = s.replace(s[0], '1')
        s = s.replace(s[1], '1')
    r = int(s, 2)
    if r > 55:
        print(n)
        break