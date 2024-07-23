n = int(input())
for _ in range(1, n + 1):
    if (n % 2 == 0) or (n % 3 == 0):
        print(1, end=' ')
    else:
        print(0, end=' ')