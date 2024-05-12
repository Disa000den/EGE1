from ipaddress import *
cnt = 0
for ip in ip_network('192.168.32.160/' '255.255.255.240'):
    b_ip = bin(int(ip))[2:].zfill(32)
    if b_ip.count('1') % 2 == 0:
        cnt += 1
print(cnt)