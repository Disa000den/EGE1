s = '2' + '0' * 1348
while '2' in s or '200' in s:
    if '200' in s:
        s = s.replace('200', '0002', 1)
    else:
        s = s.replace('2', '00', 1)
print(s.count('0'))