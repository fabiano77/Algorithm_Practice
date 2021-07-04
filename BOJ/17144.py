import copy
r, c, t = map(int, input().split())
my_map = []
for _ in range(r):
    my_map.append(list(map(int, input().split())))

def print_2d(map):
    for row in map:
        for item in row:
            print(f'{item:3}', end = ' ')
        print()
    print()
    
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]
def spread(x, y, prev_map, next_map):
    if prev_map[x][y] == 0 or prev_map[x][y] == -1:
        return
    next_map[x][y] += prev_map[x][y]
    val = prev_map[x][y]//5
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if prev_map[nx][ny] == -1:
            continue
        next_map[nx][ny] += val
        next_map[x][y] -= val

def purifying(origin_x, origin_y, prev_map, next_map):
    x, y = origin_x, origin_y + 1
    next_map[x][y] = 0
    for d in [1, 0, 3, 2]:
        nx = x + dx[d]
        ny = y + dy[d]
        while nx >= 0 and ny >= 0 and nx < r and ny < c and prev_map[nx][ny] != -1:
            next_map[nx][ny] = prev_map[x][y]
            x, y = nx, ny
            nx = x + dx[d]
            ny = y + dy[d]
    x, y = origin_x + 1, origin_y + 1
    next_map[x][y] = 0
    for d in [1, 2, 3, 0]:
        nx = x + dx[d]
        ny = y + dy[d]
        while nx >= 0 and ny >= 0 and nx < r and ny < c and prev_map[nx][ny] != -1:
            next_map[nx][ny] = prev_map[x][y]
            x, y = nx, ny
            nx = x + dx[d]
            ny = y + dy[d]

purifier = 0
for i in range(r):
    if my_map[i][0] == -1:
        purifier = i
        break

        
for _ in range(t):
    next_map = [[0] * c for _ in range(r)]
    next_map[purifier][0] = -1
    next_map[purifier+1][0] = -1
    for i in range(r):
        for j in range(c):
            spread(i, j, my_map, next_map)
    my_map = next_map
    copy_map = copy.deepcopy(my_map)
    purifying(purifier, 0, my_map, copy_map)
    my_map = copy_map

ans = 0
for i in range(r):
    for j in range(c):
        if my_map[i][j] == -1:
            continue
        ans += my_map[i][j]
print(ans)