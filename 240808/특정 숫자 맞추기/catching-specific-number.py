while True:
    i = int(input())
    if i < 25:
        print('Higher')
    elif i > 25:
        print('Lower')
    elif i == 25:
        print('Good')
        break