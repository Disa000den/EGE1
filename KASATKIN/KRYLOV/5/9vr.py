for n in range(1000, 100, -1):
    s = str(n)
    fr = s[0]
    sc = s[1]
    th = s[2]
    kv1 = int(fr) ** 2 + int(sc) ** 2
    kv2 = int(sc) ** 2 + int(th) ** 2
    s = str(max(kv1, kv2)) + str(min(kv1, kv2))
    if s == '9752':
        print(n)
        break