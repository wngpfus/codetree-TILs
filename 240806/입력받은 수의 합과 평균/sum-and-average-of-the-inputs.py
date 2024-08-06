n = int(input())
sum_val = 0
avg_val = 0

for i in range(n):
    i = int(input())
    sum_val += i

avg_val = sum_val / n
print(sum_val, end=' ')
print(f"{avg_val:.1f}")