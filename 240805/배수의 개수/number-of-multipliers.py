cnt = 0  
cntt = 0

for _ in range(10):
    num = int(input())
    if num % 3 == 0:  
        cnt += 1  
    if num % 5 == 0:
        cntt += 1

print(cnt, end=' ')
print(cntt)