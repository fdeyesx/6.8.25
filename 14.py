def f(n):
    s9 = ''
    while n!=0:
        s9 = str(n%7) + s9
        n //= 7
    return s9

s0 = 15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809
s = f(s0)
for i in '0246':
    s = s.replace(i,'+')
for i in '135':
    s = s.replace(i,'-')

print(s.count('-') - s.count('+'))
