import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lines = []
for _ in range(n):
    start, end = map(int, input().split())
    lines.append((start, end))
lines.sort()

total = 0
start, end = -1000000000, -1000000000
for line in lines:
    line_start, line_end = line
    if line_start <= end:
        # 기존의 직선 연장
        if line_end > end:
            total += line_end - end
            end = line_end
    else:
        total += line_end - line_start
        start = line_start
        end = line_end
print(total)