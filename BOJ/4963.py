import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def bfs(start):
    global n, m
    x, y = start
    if visited[x][y] or not data[x][y]:
        return 0
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if data[nx][ny] == 0:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
    return 1


while True:
    cnt = 0
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    visited = [[False]*m for _ in range(n)]
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            cnt += bfs((i, j))
    print(cnt)