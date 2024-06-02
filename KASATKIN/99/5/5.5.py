for n in range(100, 1000):
    n = str(n)
    fr = str(n[0])
    sc = str(n[1])
    th = str(n[2])
    um1 = int(fr) * int(sc)
    um2 = int(sc) * int(th)
    s = str(max(um1, um2)) + str(min(um1, um2))
    if s == '205':
        print(n)