count = 0
s = 125 + 25 ** 3 + 5 ** 9
while s > 0:
    if s % 5 == 0:
        count += 1
    s = s // 5
print(count)