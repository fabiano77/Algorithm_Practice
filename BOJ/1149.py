import sys
n = int(input())
# 빨, 초, 파
'''
26 40 83
49 60 57
13 89 99
'''
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
d = [[0] * 3 for _ in range(n)]
d[0] = lst[0]

for i in range(1, n):
    for j in range(3):
        a = (j+1)%3
        b = (j+2)%3
        d[i][j] = lst[i][j] + min(d[i-1][a], d[i-1][b])
print(min(d[n-1]))