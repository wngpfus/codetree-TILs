# a, b = map(int, input().split())

# sum = 0

# if a <= b:
#     for i in range(a, b + 1):
#         if i % 5 == 0:
#             sum += i
# else:
#     for i in range(b, a + 1):
#         sum += i 

# print(sum)

a, b = map(int, input().split())

sum = 0

# 작은 값이 항상 a가 되도록 합니다.
if a > b:
    a, b = b, a

for i in range(a, b + 1):
    if i % 5 == 0:
        sum += i

print(sum)