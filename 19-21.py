def f(s,m):
    if s >= 471: return m%2 == 0
    if m == 0: return 0
    h = [f(s+4,m-1), f(s+7,m-1), f(s*4,m-1)]
    return any(h) if m%2 == 0 else all(h)

print('19:', len([s for s in range(1,471) if not f(s,1) and f(s,2) ]))
a = [s for s in range(1,471) if not f(s,1) and f(s,3) ]
print('20:', min(a), max(a))
b = [s for s in range(1,471) if not f(s,2) and f(s,4) ]
print('21:', sum(b))
print(b)
