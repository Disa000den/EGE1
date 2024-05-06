cnt = 0
def f(x, y, a):
    return ((x < a) <= ((x ** 2) < 100)) and (((y ** 2) <= 64) <= (y <= a))
for a in range(1000):
    if all(f(x, y, a) for x in range(100) for y in range(100)):
        cnt += 1
        print(a)
print(cnt)