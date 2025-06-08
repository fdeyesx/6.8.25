from itertools import *
k = 0
for i in product('0123456789abc',repeat=7):
    s = ''.join(i)
    if s[0] != '0':
        if len(list(s)) == len(set(s)):
            for j in '13579':
                s = s.replace(j,'+')
            if '+b' not in s:
                if 'b+' not in s:
                    print(s)
                    k+=1
print(k)
