n = int(input())
satisefite = True
i = 2

while i < n:
    if n % i == 0:
        satisefite = False
        break
    i += 1
if satisefite == True:
    print('P')
else:
    print('C')