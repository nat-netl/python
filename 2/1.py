# ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y)

print ("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if((x and y) <= ((not z) or w) and ((not w) <= x) or (not y)) == 0:
                    print (x, y, z, w)