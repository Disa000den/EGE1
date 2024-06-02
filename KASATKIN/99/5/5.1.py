for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = s + '00'
    else:
        s = s + '11'
    r = int(s, 2)
    if r > 115:
        print(n)
        break