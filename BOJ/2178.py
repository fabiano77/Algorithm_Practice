n, m = map(int, input().split())

land = []
for _ in range(n):
    land.append(list(map(int, input())))
visited = [[False]*n for _ in range(n)]
def print_2d(m):
    for i in m:
        print(i)
    print()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

from collections import deque
def bfs(land):
    queue = deque()
    queue.append([0, 0])
    while queue:
        p = queue.popleft()
        
        x, y = p[0], p[1]
        # 방문처리 -> 거리 증가

        # 해당 점과 연결된 점을 방문.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) == (0, 0)or nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            # 가지 않은 경로 or 더 짧은 경로일 경우
            if land[nx][ny] == 1 or land[nx][ny] > land[x][y] + 1:
                land[nx][ny] = land[x][y] + 1
                queue.append([nx, ny])

bfs(land)
print(land[n-1][m-1])