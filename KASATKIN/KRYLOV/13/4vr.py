from ipaddress import *
cnt = 0
for i in ip_network(f'253.112.169.12/255.255.254.0', 0):
    s = f'{i:b}'
    if s[16:].count('1') >= s[:16].count('1'):
        cnt += 1
print(cnt)