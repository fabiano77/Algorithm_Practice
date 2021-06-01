import sys
input = lambda: sys.stdin.readline().rstrip()

def is_included(x, y, r, target_x, target_y):
    if (((target_x - x)**2 + (target_y - y)**2)**0.5) <= r:
        return True
    else:
        return False

def xor(a, b):
    if (a and not b) or (not a and b):
        return True
    else:
        return False

t = int(input())

for _ in range(t):
    x_s, y_s, x_e, y_e = map(int, input().split())
    n = int(input())
    ans = 0
    for _ in range(n):
        x, y, r = map(int, input().split())
        if xor(is_included(x, y, r, x_s, y_s), is_included(x, y, r, x_e, y_e)):
            ans += 1
    print(ans)

