from ipaddress import *
cnt = 0
for ip in ip_network(f'142.108.56.118/255.255.255.240', 0):
    bip = f'{ip:b}'
    if bip[16:].count('1') > bip[:16].count('1'):
        cnt += 1
print(cnt)
