for x in ('0123456789abcdefghijklm'):
    x1 = '1' + x + '1' + x + '1' + x + '1' + x + '1'
    x2 = '20' + x + '24'
    x3 = '1' + x + '235'
    res = int(x1, 23) + int(x2, 23) + int(x3, 23)
    if res % 22 == 0:
        print(x, int(res // 22))