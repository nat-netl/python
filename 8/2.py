a = "АБВГ"

num = 0

for l1 in a: 
    for l2 in a: 
        for l3 in a: 
            for l4 in a: 
                for l5 in a: 
                    w = l1 + l2 + l3 + l4 + l5
                    if (w.count("А") == 1):
                        num += 1

print (num)