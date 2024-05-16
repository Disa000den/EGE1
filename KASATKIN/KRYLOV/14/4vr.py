for x in ('0123456789abcdefghi'):
    x1 = '3' + x + '2' + x + '1' + x + '0' + x + '1'
    x2 = x + '2024'
    x3 = '1' + x + '077'
    res = int(x1, 19) + int(x2, 19) + int(x3, 19)
    if res % 18 == 0:
        print(x, res // 18)