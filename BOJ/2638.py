n, m = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(n)]
contact_side_map = [[0]*m for _ in range(n)]

time = 0

dx = [-1, 0, +1, 0]     
dy = [0, +1, 0, -1]     # 상 우 하 좌

from collections import deque

def check_contact():
    q = deque([(0, 0)])
    contact_side_map[0][0] = -1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if contact_side_map[nx][ny] == -1:
                continue
            if my_map[nx][ny] == 1:
                contact_side_map[nx][ny] += 1
            else:
                q.append((nx, ny))
                contact_side_map[nx][ny] = -1

def melt_and_reset():
    for i in range(n):
        for j in range(m):
            if contact_side_map[i][j] >= 2:
                my_map[i][j] = 0
            contact_side_map[i][j] = 0

def all_zero():
    ret = True
    for i in range(n):
        for j in range(m):
            if my_map[i][j] != 0:
                ret = False
    return ret

while not all_zero():
    check_contact()
    melt_and_reset()
    time += 1
print(time)