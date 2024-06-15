from itertools import permutations

count = 0

def f(s):
    for p in permutations(s):
        if p[0]+p[1] == p[2]+p[3]:
            return True
    return False

for line in open("11111.txt"):
    a = [int(x) for x in line.split()]
    maxA = max(a)

    p = [x for x in a if x != maxA]
    pSum = sum(p)

    if (maxA < pSum and f(a)):    
        count += 1


print(count)