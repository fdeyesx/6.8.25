def d(x1,y1,x2,y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def centre(k):
    mn = 10**10
    for i in range(len(k)):
        tx,ty = k[i][0], k[i][1]
        s = 0
        for j in range(len(k)):
            cx, cy = k[j][0], k[j][1]
            s += d(tx,ty,cx,cy)
        if s < mn:
            mn = s
            cntx = tx
            cnty = ty
    return [cntx,cnty]

print('file a:')
s = open('27.1/27A (3).txt').readlines()
ak1,ak2 = [],[]
for i in s:
    r = i.split()
    x,y = float(r[0]),float(r[1])
    if y > 10: ak1.append([x,y])
    else: ak2.append([x,y])

x1,y1 = centre(ak1)
x2,y2 = centre(ak2)

print( (x1+x2)/2 * 10_000)
print( (y1+y2)/2 * 10_000)

print('file b:')
s = open('27.1/27B (3).txt').readlines()
bk1,bk2,bk3 = [],[],[]
for i in s:
    r = i.split()
    x,y = float(r[0]),float(r[1])
    if y > 20: bk1.append([x,y])
    else:
        if y > 10: bk2.append([x,y])
        else: bk3.append([x,y])

x1,y1 = centre(bk1)
x2,y2 = centre(bk2)
x3,y3 = centre(bk3)

print( (x1+x2+x3)/3 * 10_000)
print( (y1+y2+y3)/3 * 10_000)
