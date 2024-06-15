# ((x → y) ∨ (y ≡ w)) ∧ ((x ∨ z) ≡ w)
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                    if ((x <= y) or (y == w)) and ((x or z) == w):
                        print(x, y, z, w)
                        # x y z w
                        # 0 0 1 1
                        # 0 1 0 0
                        # 0 1 1 1
                        # 1 1 0 1   