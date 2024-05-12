n = 5 ** 94 + 25 ** 49 - 130
cnt = 0
while n > 0:
    if n % 5 == 4:
        cnt += 1
    n = n // 5
print(cnt)