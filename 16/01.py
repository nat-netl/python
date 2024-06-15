# 1
# def F(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0 :
#         return F(n / 2)
#     if n % 2 != 0:
#         return 1 + F(n - 1)

# cnt = 0
# for n in range(1, 1000):
#     if (F(n)) == 3:
#         cnt+=1

# print(cnt)

# 6
# def F(n):
#     if n>=2025:
#         return n
#     if n < 2025:
#         return n + 3 + F(n + 3)
    
# print (F(23) - F(21))

# 9
# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n>2 and n % 2 == 0:
#         return (4*n-F(n-3))/8
#     if n>2 and n % 2 != 0:
#         return (4*n-F(n-1) + F(n-2))/8

# print (F(52)-F(38))

# 15
# def F(n):
#     if n>2024:
#         return n
#     if n <= 2024:
#         return n*F(n+1)
    
# print (F(2022) / F(2024))


# Алгоритмы
# 1

# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 3
#     if n>2:
#         return F(n-1) * n + F(n-2) * (n - 1)

# print (F(5))

# 4
# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return F(n-2) + F(n-1)
    
# print(F(8))


# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n-1) * (n+1)

# print(F(4))

def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return F(n - 2) * (n + 1)
    
print(F(8))