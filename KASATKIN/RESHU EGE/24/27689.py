f = open('27689.txt')
s = f.readline()
count = 1
mx = 0
s = s.replace('XYZ' , '***')
if '*X' in s:
    s = s.replace('*X', '**')
for i in range(len(s) - 1):
    if s[i] == '*' and s[i + 1] == '*':
        count += 1
        mx = max(count, mx)
    else:
        count = 1
print(mx)