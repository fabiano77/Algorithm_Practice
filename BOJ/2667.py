n = int(input())

land = []
for _ in range(n):
    land.append(list(map(int, input())))
visited = [[False] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
number = 1
def dfs(x, y, cnt):
    global n
    global land
    global visited
    if land[x][y] == 0 or visited[x][y] == True:
        return 0
    visited[x][y] = True
    cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
            continue
        cnt += dfs(nx, ny, cnt)
    return cnt

cnt_list = []
# 탐색 시작
for i in range(n):
    for j in range(n):
        t = dfs(i, j, 0)
        if t > 0:
            cnt_list.append(t)
cnt_list.sort()
print(len(cnt_list))
for item in cnt_list:
    print(item)

