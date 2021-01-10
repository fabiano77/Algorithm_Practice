n, r, c = map(int, input().split())

# n이 1이면 2x2 4이면 16x16

def solve(n, x, y):
    if n == 0:
        return 0
    # 사분면의 길이
    length = 2 ** (n-1)
    # print('solve(', n, x, y,')')
    # print('len =', length)
    # 좌상단
    if x < length and y < length:
        return solve(n-1, x, y)
    # 우상단
    elif x < length and y >= length:
        return solve(n-1, x, y - length) + 1*(length ** 2)
    # 좌하단
    elif x >= length and y < length:
        return solve(n-1, x - length, y) + 2*(length ** 2)
    # 우하단
    elif x >= length and y >= length:
        return solve(n-1, x - length, y - length) + 3*(length ** 2)

print(solve(n, r, c))