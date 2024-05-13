for n in range(1, 1000):
    s = bin(n)[2:]
    s = str(s)
    if s[-1] == '0':
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    r = int(s, 2)
    if r > 52:
        print(n)
        break
