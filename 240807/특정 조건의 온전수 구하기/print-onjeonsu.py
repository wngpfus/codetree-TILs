a = int(input())

for i in range(1, a + 1):
    if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
        continue
    else:
        print(i, end=' ')