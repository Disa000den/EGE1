def f(n):
    s = bin(n)[3:]
    c = int(s, 2)
    return n - c


a = []
for n in range(100, 3001):
    if f(n) not in a:
        a.append(f(n))
print(len(a))
