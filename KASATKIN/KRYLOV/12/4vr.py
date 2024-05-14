for n in range(3, 10001):
    s = '4' + '1' * n
    while '31' in s or '411' in s or '1111' in s:
        if '31' in s:
            s = s.replace('31', '1', 1)
        if '411' in s:
            s = s.replace('411', '13', 1)
        if '1111' in s:
            s = s.replace('1111', '4', 1)
    r = sum(map(int, s))
    if r == 34:
        print(n)