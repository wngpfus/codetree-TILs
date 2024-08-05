a = int(input())
sum_val = 0

for i in range(a):
    n = int(input())
    if n % 2 == 1 and n % 3 == 0:
        sum_val += n
print(sum_val)