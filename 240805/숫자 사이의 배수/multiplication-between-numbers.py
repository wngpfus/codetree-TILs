# a, b = map(int, input().split())

# sum_val = 0
# sum_a
# for i in range(a, b + 1):
#     if a % 5 == 0 or a % 7 == 0:
#         sum_val += 1
#         sum_a = 


a, b = map(int, input().split())

# 5 또는 7의 배수들의 합과 개수를 저장할 변수
sum_val = 0
count = 0

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        count += 1

# 평균 계산
if count > 0:
    average = sum_val / count
else:
    average = 0

# 합과 평균 출력
print(sum_val, round(average, 1))