n = 3 ** 2020 - 3 ** 1020 + 9 ** 800 - 81
cnt = 0
while n > 0:
    if n % 3 == 2:
        cnt += 1
    n = n // 3
print(cnt)