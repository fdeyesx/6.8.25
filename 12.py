for n in range(4, 1000):
    s = '>'+ '0'*25 + '1'*n + '2'*25
    while '>1' in s or '>2' in s or '>0':
        s = s.replace('>1','22>',1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>0', '1>', 1)
    sum1 = s.count('1') + s.count('2')*2
    if 999 < sum1 < 10_000:
        if sum1%15 == 0:
            print(n)
            break
