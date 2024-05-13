for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'
    if s.count('1') % 3 == 0:
        s = '11' + s[2:]
    else:
        s = '11' + s[2:]
    r = int(s, 2)
    if r >= 26:
        print(n)
