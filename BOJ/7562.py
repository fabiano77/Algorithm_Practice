from collections import deque

t = int(input())

dx = [-2, -1, +1, +2, +2, +1, -1, -2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]

def solve(x_s, y_s, x_e, y_e, n):
    visited = [[False] * n for _ in range(n)]
    q = deque([(x_s, y_s, 0)])
    visited[x_s][y_s] = True
    while q:
        x, y, cnt = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            n_cnt = cnt + 1
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if nx == x_e and ny == y_e:
                return n_cnt
            visited[nx][ny] = True
            q.append((nx, ny, n_cnt))
    return 0

for _ in range(t):
    n = int(input())
    x_s, y_s = map(int, input().split())
    x_e, y_e = map(int, input().split())
    print(solve(x_s, y_s, x_e, y_e, n))

    