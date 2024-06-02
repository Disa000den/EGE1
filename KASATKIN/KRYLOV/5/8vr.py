for n in range(1000, 1, -1):
    s = bin(n)[2:]
    if len(s) % 2 == 0:
        if s.count('1') % 2 == 0:
            s = s[:len(s) % 2] + '1' + s[len(s) % 2:]
    else:
        s = s
    r = int(s, 2)
    if r <= 26:
        print(n)