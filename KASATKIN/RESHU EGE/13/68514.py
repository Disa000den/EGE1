from ipaddress import *
cnt = 0
for ip in ip_network('122.159.136.144/' '255.255.255.248'):
    b_ip = bin(int(ip))[2:].zfill(32)
    if b_ip.count('1') % 4 != 0:
        cnt += 1
print(cnt)