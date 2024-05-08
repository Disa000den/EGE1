it = str()
for i in range(9999, 1000, -1):
    temp = str(i)
    o = int(temp[0])
    d = int(temp[1])
    t = int(temp[2])
    c = int(temp[3])
    od = o + d
    dt = d + t
    tc = t + c
    mn = min(od, dt, tc)
    if mn == od:
        it = str(min(dt, tc)) + str(max(dt, tc))
    elif mn == dt:
        it = str(min(od, tc)) + str(max(od, tc))
    elif mn == tc:
        it = str(min(od, dt)) + str(max(od, dt))
    if it == '1315':
        print(i)
        break
    else:
        it = '0'