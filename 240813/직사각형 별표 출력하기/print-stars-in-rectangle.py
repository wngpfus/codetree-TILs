# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*', end='')
#     print()

n, m = map(int, input().split())
for i in range(n):
    for i in range(m):
        print('*', end=' ')
    print()