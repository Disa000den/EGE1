for n in range(1, 1000):
    s = bin(n)[2:]
    if 6 <= len(s) <= 7:
        if s.count('1') % 2 == 0:
            s = s + '1'
            print(s, n, 'chet')
        else:
            s = s + '11'
            print(s, n, 'nechet')