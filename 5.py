def main(n):
    s = str(bin(n))[2:]
    if len(s)% 2 == 0:
        r = len(s)//2
        s = s[:r] + '010' + s[r:]
    else:
        r = (len(s) // 2) + 1
        s = s[:r] + '101' + s[r:] + s[-1]
    return int(s,2)

a = []
for n in range(0,100000):
    r = main(n)
    if r > 414:
        a.append(r)
print(min(a))
