def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 != 0:
        return f(n - 1) + 1
    if n % 2 == 0:
        return f(n / 2)
count = 0
it = 0
for n in range(1_000_000_000, 1, -1):
    it += 1
    print('Количество итераций =', it)
    if f(n) == 3:
        count += 1
print('Итоговое число =', count)