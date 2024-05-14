cnt = 0
for a in range(1, 5):
    for b in range(5):
        for c in range(5):
            if a > b > c:
                cnt += 1
print(cnt)