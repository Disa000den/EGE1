for n in range(1, 1000):
    ch = n
    s = '>' + '0' * 15 + '1' * n + '2' * 15
    while '>0' in s or '>1' in s or '>2' in s:
        if '>0' in s:
            s = s.replace('>0', '22>', 1)
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '1>', 1)
    s = s[:len(s) - 1]
    r = sum(map(int, s))
    print(r, ch)

