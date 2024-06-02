for n in range(2, 1000):
    s = bin(n)[2:]
    s = s + s[-2]
    s = s + s[1]
    r = int(s, 2)
    if r > 170:
        print(n)
        break