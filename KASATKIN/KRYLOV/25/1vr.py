from fnmatch import *
for n in range(31007, 10 ** 10, 31007):
    if fnmatch(str(n), '1*34?5?9'):
        print(n, n // 31007)