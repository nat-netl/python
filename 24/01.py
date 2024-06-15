s = open("24_2024.txt").readline()

w = s.split("T")
m = 0
for i in range(len(w)-101):
    a = "T".join(w[i:i+101])
    m = max(len(a), m)

print(m)