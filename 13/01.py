for x in "0123456789ABCD":
    if (int ("321" + x + "4", 19) + int ("498" + x + "9", 19)) % 23 == 0:
        print(x, (int ("321" + x + "4", 19) + int ("498" + x + "9", 19)) // 23)