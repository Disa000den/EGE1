print ('x, y, z, F')
for x in range (0,2):
    for y in range (0,2):
        for z in range(0, 2):
            F = (not z) and x or x and y
            if F == 1:
                print(x, y, z, int(F))
