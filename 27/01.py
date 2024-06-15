f = open ("27A_59854.txt")
n = int(f.readline())
a = [int(s) for s in f]

max_sum = 0

for i in range (n):
    for j in range(i+1, n):
        max_sum = max(max_sum, a[i] + a[j] + (j-i))


print (max_sum)