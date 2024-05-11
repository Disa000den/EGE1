for x in '0123456789abcdefghijkl':
    x1 = '63' + str(x) + '59685'
    x2 = '17' + str(x) + '53'
    x3 = '36' + str(x) + '5'
    res = int(x1, 22) + int(x2, 22) + int(x3, 22)
    if res % 21 == 0:
        res = res // 21
        print(res)