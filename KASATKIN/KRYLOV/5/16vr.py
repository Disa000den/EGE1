for n in range(1000, 1, -1):
    ch = n
    n = ch - (ch % 4)
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = s + '01'
    else:
        s = s + '10'
    r = int(s, 2)
    if r < 47:
        print(ch)