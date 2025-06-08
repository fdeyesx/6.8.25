for a in range(0,1000):
    d = set()
    for x in range(0,2000):
        for y in range(0,2000):
            f = (x**2 <= 136) or (y < (4*x + a - 70)) or (2*y > 51)
            d.add(f)
    if False not in d:
        print(a)
        break
