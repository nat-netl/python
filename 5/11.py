list = []
for n in range(100, 1000):
    ns = str(n)
    n1 = int(ns[0]) + int(ns[1])
    n2 = int(ns[1]) + int(ns[2])

    s1 = str(max(n1, n2))
    s2 = str(min(n1, n2))


    res = s1 + s2
    if res == "1412":
        print (n)