it = str()
for i in range(9999, 1000, -1):
    temp = str(i)
    o = int(temp[0])
    d = int(temp[1])
    t = int(temp[2])
    c = int(temp[3])
    print(o, d, t, c)
    od = o + d
    dt = d + t
    tc = t + c
    print(od, dt, tc)
    mn = min(od, dt, tc)
    if mn == od:
        it = min(dt, tc) + max(dt, tc)
    elif mn == dt:
        it = min(od, tc) + max(od, tc)
    elif mn == tc:
        it = min(od, dt) + max(od, dt)
    if it == '1315':
        print(i)
    else:
        it = '0'