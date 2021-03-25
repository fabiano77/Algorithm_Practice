import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())

# 작업시간, 작업시간, 이동시간, 이동시간

ans = 0


data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(len(data)-1):
    next_a = min(data[i][0] + data[i+1][0], data[i][1] + data[i][3] + data[i+1][0])
    next_b = min(data[i][1] + data[i+1][1], data[i][0] + data[i][2] + data[i+1][1])
    data[i+1][0] = next_a
    data[i+1][1] = next_b

print(min(data[-1]))