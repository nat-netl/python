for a in range (1000):
    if all((y + 2 * x != 48) or (a < x) or (a < y) for x in range (1000) for y in range (1000)):
        print (a)
        