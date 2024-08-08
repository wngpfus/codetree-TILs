while True:
    a, b, c = map(str, input().split())
    a = int(a)
    b = int(b)
    sum_val = a * b
    print(sum_val)
    if c == 'C':
        break