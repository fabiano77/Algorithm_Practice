for _ in range(int(input())):
    a, b = map(int, input().split())
    x, y = max(a, b), min(a, b)
    while y:
        x, y = y, x%y
    print(a*b//x)