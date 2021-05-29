n, m = map(int, input().split())

# 세로길이 n, 가로길이 m

if n == 1:
    print(1)
elif n == 2:
    if m >= 7:
        print(4)
    elif m >= 5:
        print(3)
    elif m >= 3:
        print(2)
    else:
        print(1)
else:
    if m >= 7:
        print(1+4+(m-7))
    elif m <= 4:
        print(1+(m-1))
    else:
        print(4)

