for x in '0123456789abcdefg':
    x1 = '8' + str(x) + '5678'
    x2 = '457' + str(x) + '69'
    x3 = '145' + str(x) + '1'
    res = int(x1, 25) + int(x2, 25) + int(x3, 25)
    if res % 23 == 0:
        res = res // 23
        print(res)
