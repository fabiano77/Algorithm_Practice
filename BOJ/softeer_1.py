import sys

input = lambda: sys.stdin.readline().rstrip()

k, p, n = map(int, input().split())

# 1초당 p배

ans = k

for _ in range(n):
    ans = (ans * p) % 1000000007

print(ans)