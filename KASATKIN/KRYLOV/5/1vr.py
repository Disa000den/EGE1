for n in range(1000, 10, -1):
    ch = n
    b = ''
    while n > 0:
        b = str(n % 4) + b
        n = n // 4
    if ch % 4 != 0:
        ost = (ch % 4) * 2
        c = ''
        while ost > 0:
            c = str(ost % 4) + c
            ost = ost // 4
        b = b + c
    else:
        b = b + b[-2] + b[-1]
    r = int(b, 4)
    if r < 261:
        print(ch)