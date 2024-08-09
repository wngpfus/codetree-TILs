a, b = map(int, input().split())
satisefite = False

for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        satisefite = True
if satisefite == True:
    print(1)
else:
    print(0)