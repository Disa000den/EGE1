from itertools import *
cnt = 0
for p in product('0123456789', repeat=6):
    s = ''.join(p)
    if int(s) % 5 == 0 and s[0] != '0' and len(set(s)) == len(s):
        s = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
        s = s.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        if '11' not in s and '22' not in s:
            cnt+= 1
print(cnt)