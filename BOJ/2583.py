from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

m, n, k = map(int, input().split())

mymap = [[False]*(n) for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            mymap[y][x] = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque([[x, y]])
    cnt = 1
    mymap[x][y] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if mymap[nx][ny] == True:
                continue
            queue.append([nx, ny])
            mymap[nx][ny] = True
            cnt += 1
    return cnt

ans = []
for i in range(m):
    for j in range(n):
        if not mymap[i][j]:
            ans.append(bfs(i, j))

print(len(ans))
for item in sorted(ans):
    print(item, end=' ')