
# 28x2 18 + 93x5 12


for x in range (0, 9):
    if ((2*18**3 + 8*18**2 + x*18**1 + 2*18**0) + (9*12**3 + 3*12**2 + x*12**1 + 5*12**0)) % 133 == 0 :
        print (x, ((2*18**3 + 8*18**2 + x*18**1 + 2*18**0) + (9*12**3 + 3*12**2 + x*12**1 + 5*12**0)) // 133)
        break