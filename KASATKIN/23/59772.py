def f(x, y):
    if x > y or x == 9 or x == 15:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 3, y) + f(x * 3, y)


print(f(3, 18))