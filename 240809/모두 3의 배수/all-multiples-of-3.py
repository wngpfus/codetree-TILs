satisefite = False
cnt = 0

for i in range(5):
    n = int(input())
    if n % 3 == 0:
        cnt += 1
    elif cnt == 5:
        satisefite = True
if satisefite == True:
    print(0)
else:
    print(1)