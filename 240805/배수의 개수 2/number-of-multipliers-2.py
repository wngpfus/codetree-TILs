cnt = 0  # 홀수의 개수를 저장할 변수

# 10개의 숫자를 입력받아 처리
for _ in range(10):
    num = int(input())
    if num % 2 != 0:  # 입력된 숫자가 홀수인 경우
        cnt += 1  # cnt를 1 증가

# 결과 출력
print(cnt)