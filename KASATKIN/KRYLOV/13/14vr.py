from ipaddress import *
for a in range(1, 256):
    fl = True
    for i in ip_network(f'126.255.{a}.100/255.255.240.0', 0):
        s = f'{i:b}'
        if s[:16].count('1') < s[16:].count('1'):
            fl = False
    if fl == True:
        print(a)