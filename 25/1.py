for a in range (1991, 10 ** 8 + 1, 1991):
    s = str(a)

    if s[0] == "3" and s[2] == "1" and s[-2] == "5" and s[-1] == "7":
        print (a, a // 1991)