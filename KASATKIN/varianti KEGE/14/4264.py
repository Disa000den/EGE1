n = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27
cnt = 0
while n > 0:
    if n % 3 == 2:
        cnt += 1
    n = n // 3
print(cnt)