k = 0
for x in range(345_678,10**10):
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    d = sorted(d)
    b = []
    for i in d:
        if int(i)%2 != 0:
            b.append(i)
    f = sum(b)//len(b)
    if f != 0:
        if f%37 == 0:
            k+=1
            print(x, f)
            if k == 5:
                break
