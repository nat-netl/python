def f (x, end):
    if x > end: return 0
    if x == 11: return 1
    if x == end: return 1
    return f(x + 2, end) + f(x * 2, end) + f(x + 3, end)

print (f(2, 11) * f(2, 11)) 