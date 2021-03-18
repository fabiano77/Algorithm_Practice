import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = [list(input()) for _ in range(n)]
visited = [[False]* n for _ in range(n)]
RG_visited = [[False]* n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(point, visited, RG_mode):
    x, y = point
    if visited[x][y]:
        return 0
    queue = deque([point])
    visited[x][y] = True
    color = data[x][y]
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if not RG_mode and data[nx][ny] != color:
                continue
            if RG_mode and ((data[nx][ny] in 'RG' and color == 'B') or (data[nx][ny] == 'B' and color in 'RG')):
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
    return 1

a = 0
b = 0
for i in range(n):
    for j in range(n):
        a += bfs((i, j), visited, 0)
        b += bfs((i, j), RG_visited, 1)
print(a, b)