for n in range(10, 1000):
    ch = n
    b = ''
    while n > 0:
        b = str(n % 4) + b
        n = n // 4
    if ch % 4 == 0:
        b = b + b[-1] + b[-2]
    else:
        ost = (ch % 4) * 2
        c = ''
        while ost > 0:
            c = str(ost % 4) + c
            ost = ost // 4
        b = b + c
    r = int(b , 4)
    if r >= 1088:
        print(ch)