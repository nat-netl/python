# /1
# f = open ("17.txt")
# a = []
# for s in f:
#     a.append(int(s))

# summ_par = []
# for i in range (len(a) - 1):
#     if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
#         summ_par.append(a[i]+a[i+1])

# print (len(summ_par), max(summ_par))

# /2

# f = open ("2.txt")
# a = []

# for s in f: 
#     a.append(int(s))

# sum_par = []

# for i in range (len(a)-1):
#     if (a[i] % 160) != (a[i + 1] % 160) and a[i] % 7 == 0 or a[i+1] % 7 == 0:
#         sum_par.append(a[i]+a[i+1])

# print (len(sum_par), max(sum_par))

# f = open("3.txt")
# count = 0
# sum_par = []
# a = []

# for s in f: 
#     a.append(int(s))

# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if (a[i] - a[j]) % 2 == 0 and (a[i] % 31 == 0 or a[j] % 31 == 0):
#             sum_par.append (a[i] + a[j])

# print(len(sum_par), max(sum_par))

# .16
# f = open ("16.txt")

# a = [int (s) for s in f]
# sum_par = []

# for i in range (len(a) - 1):
#     for j in range (i + 1, len (a)):
#         if (a[i] + a[j]) % 117 == 0:
#             sum_par.append (a[i] + a[j])

# print (len (sum_par), max(sum_par))


s = [int(x) for x in open("17.txt")]

m = min([x for x in s if abs(x)%10==abs(x)%100])
res = []

for i in range (len(s) - 1):
    for j in range (i + 1, len(s)):
        if (str(s[i])[-1:] == str(s[j])[-2:] or str(s[j])[-1:] == str(s[i])[-2:]) and (s[i] % 7 != 0 or s[j] % 7 != 0) and (s[i]**2 + s[j]**2 <= m):
            res.append(s[i] + s[j])

print(res)