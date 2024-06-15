# F1  =  (w ∨¬ y) → (z ≡ x)
# F2  =  (w ∨¬ y) ≡ (x → z)
print ("x y z w")
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                if (w or (not y)) <= (z == x):
                    print (x,y,z,w)
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                if (w or (not y)) == (x <= z):
                    print (x,y,z,w)