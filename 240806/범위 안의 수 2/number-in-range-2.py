sum_val = 0
avg = 0
cnt = 0

for i in range(10):
    i = int(input())
    if i >= 0 and 200 >= i:
        sum_val += i
        cnt += 1

avg = sum_val / cnt
print(sum_val, end=' ')
print(f"{avg:.1f}")