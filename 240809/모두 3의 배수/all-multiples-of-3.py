satisefite = False
cnt = 0

for i in range(5):
    n = int(input())
    if n % 3 == 0:
        cnt += 1
        if cnt == 5:
            satisefite = True
            break  # 조건이 만족되면 더 이상 반복할 필요가 없으므로 반복문을 종료합니다.

if satisefite:
    print(1)
else:
    print(0)