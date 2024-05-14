from ipaddress import *
for a in (0, 128, 192, 224, 240, 248, 252, 254, 255):
    t = True
    for i in ip_network(f'255.211.33.160/255.255.{a}.0', 0):
        s = f'{i:b}'
        if s[:16].count('1') < s[16:].count('1'):
            t = False
    if t == True:
        print(a)