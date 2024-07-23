n = int(input())
for i in range(n, 101):
    if n >= 90:
        print('A', end=' ')
        n += 1
    elif n >= 80:
        print('B', end=' ')
        n += 1
    elif n >= 70:
        print('C', end=' ')
        n += 1
    elif n >= 60:
        print('D', end=' ')
    else:
        print('F', end=' ')