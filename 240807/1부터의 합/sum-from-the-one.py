n = int(input())
s = 0

for i in range(1, 101):
    s += i
    if s >= n:
        break
print(i)