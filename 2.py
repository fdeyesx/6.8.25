print('x | y | z | w | f')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not(not(z <= y) or (x == w) or x)
                if f == 1:
                    print(x,y,z,w,f,sep=' | ')
