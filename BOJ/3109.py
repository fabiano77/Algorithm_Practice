r, c = map(int, input().split())
mymap = [list(map(str, input())) for _ in range(r)]

dx = [1, 0, -1]
dy = [1, 1, 1]

def dfs(start_point):
    global cnt
    global r, c
    x, y = start_point
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        mymap[x][y] = 'x'
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if mymap[nx][ny] == 'x':
                continue
            # if nx - cnt < 0 or mymap[nx-cnt][ny] == 'x':
            #    continue
            if ny == c-1:
                return 1
            stack.append((nx, ny))
    return 0

cnt = 0
for i in range(r):
    cnt += dfs((i, 0))

print(cnt)
