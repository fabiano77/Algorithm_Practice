# 문자열 분석

while True:
    try:
        data = input()
        a, b, c, d = 0, 0, 0, 0
        for ch in data:
            if ch.islower():
                a += 1
            elif ch.isupper():
                b += 1
            elif ch.isnumeric():
                c += 1
            elif ch.isspace():
                d += 1
        print(a, b, c, d)
    except EOFError:
        break