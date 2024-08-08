cnt = 0
sum_val = 0

while True:
    a = int(input())

    if a // 10 != 2:
        break

    cnt += 1
    sum_val += a

avg = sum_val / cnt

print(f"{avg:.2f}")