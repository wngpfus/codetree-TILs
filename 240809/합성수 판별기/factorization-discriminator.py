n = int(input())
satisefite = False

for i in range(2, n - 1):
    if n % i == 0:
        satisefite = True

if satisefite == True:
    print('C')
else:
    print('N')