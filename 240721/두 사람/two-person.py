aa, ax = input().split()
bb, bx = input().split()

aa = int(aa)
bb = int(bb)

if (aa >= 19 and ax == 'M') or (bb >= 19 and bx == 'M'):
    print(1)
else:
    print(0)