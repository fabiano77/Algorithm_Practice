from collections import deque

n = int(input())
my_map = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y, water):
    global visited, n
    if my_map[x][y] <= water or visited[x][y]:
        return 0 
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if my_map[x][y] <= water:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
    return 1

ans = 0
for water in range(100):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cnt += bfs(i, j, water)
    ans = max(ans, cnt)
    if cnt == 0: break
print(ans)