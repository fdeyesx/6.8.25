def f(n,e):
    if n > e or n == 27: return 0
    if n == e: return 1
    return f(n**2,e)+f(n+3,e)+f(n+5,e)

print(f(3,16)*f(16,51))
