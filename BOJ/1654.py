import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lines = []
for _ in range(n):
    lines.append(int(input()))

ans = 0
first = 0
last = max(lines)
while first <= last:
    middle = (first + last) // 2
    t = 0
    for line in lines:
        if middle == 0:
            t = k+1
        else:
            t += line // middle
    if t >= k:
        ans = max(ans, middle)
        first = middle + 1
    else:
        last = middle - 1
print(ans)

