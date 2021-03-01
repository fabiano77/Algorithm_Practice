import sys
input = lambda: sys.stdin.readline().rstrip()

m, n, h = map(int, input().split())
# m 가로, n 세로, h 높이

dx = [+1, -1, 0, 0, 0, 0]
dy = [0, 0, +1, -1, 0, 0]
dz = [0, 0, 0, 0, +1, -1]

data = []
for _ in range(h):
    layer = []
    for _ in range(n):
        layer.append(list(map(int, input().split())))
    data.append(layer)

visited = []

from collections import deque
def bfs(start, queue):
    while queue:
        x, y, z = queue.popleft()
        day = data[x][y][z]
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            if nx >= 0 and nx <= h-1 and ny >= 0 and ny <= n-1 and nz >= 0 and nz <= m-1:
                if (data[nx][ny][nz] > day + 1 or data[nx][ny][nz] == 0):
                    queue.append([nx, ny, nz])
                    data[nx][ny][nz] = day + 1



queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                queue.append([i, j, k])

bfs(data, queue)

max = 0
no = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 0:
                no = True
                break
            if data[i][j][k] > max:
                max = data[i][j][k]
    if no:
        break

if no:
    print(-1)
else:
    print(max - 1)