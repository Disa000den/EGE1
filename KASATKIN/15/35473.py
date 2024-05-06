def f(x, A):
    return (A % 45 == 0) and ((750 % x == 0) <= ((A % x != 0) <= (120 % x != 0)))


for A in range(1, 200):
    if all(f(x, A) for x in range(1, 500)):
        print(A)
        break