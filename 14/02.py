f = 4**34 + 5 * 4**22 + 4**13 + 2 * 4**9 + 82
s = set()

while f != 0: 
    s.add(f % 16)
    f //= 16
print (len(s))
