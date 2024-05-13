for n in range(1000, 1, -1):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '0'
    else:
        s += '1'
    if s.count('1') % 3 == 0:
        s = '11' + s[2:]
    else:
        s = '10' + s[2:]
    r = int(s, 2)
    if r <= 37:
        print(n)