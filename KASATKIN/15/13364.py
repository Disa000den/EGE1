s = []
for a1 in range(1, 200):
    for a2 in range(1, 200):
        fl = True
        for x in range(1, 200):
            if not((130 <= x <= 171) <= (((150 <= x <= 185) and (not (a1 <= x <= a2))) <= (not(130 <= x <= 171)))):
                fl = False
                break
        if fl:
            s.append(a2 - a1)
print(min(s))
