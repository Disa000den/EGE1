f = [1] * 2025
f[1] = 5
for n in range(2, 2025):
    f[n] = 2 * n + 1 + f[n - 1]
print(f[2024] - f[2022])