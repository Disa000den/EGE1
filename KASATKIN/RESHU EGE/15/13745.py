for a in range(500, 1, -1):
    k = 0
    for x in range(100):
        for y in range(100):
            if ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9)):
                k += 1
        if k == 100 * 100:
            print(a)
            break