from ipaddress import *

n = ip_network('98.71.254.171/255.248.0.0',0)
o = n.network_address
for i in n:
    f = f'{i:b}'
    if f.count('1')%7 == 0:
        if i != o:
            print(i)
            break
