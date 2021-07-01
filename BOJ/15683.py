import copy
n, m = map(int, input().split())
origin_map = [list(map(int, input().split())) for _ in range(n)]
cctvs = []

for i in range(n):
    for j in range(m):
        val = origin_map[i][j]
        if val != 0 and val != 6:
            cctvs.append((val, i, j))

# 0:북, 1:동, 2:남, 3:서
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]
def check_line(point, direction, my_map):
    x, y = point
    while True:
        x += dx[direction]
        y += dy[direction]
        if x < 0 or y < 0 or x >= n or y >= m:
            break
        if my_map[x][y] == 6:
            break
        my_map[x][y] = '#'

cctv_directions = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]],
                     [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]] ]

def print_2d(my_map):
    for li in my_map:
        for i in li:
            print(i, end=' ')
        print()
    print()

def check_map(my_map):
    global n, m
    cnt = 0
    for i in range(n):
        for j in range(m):
            if my_map[i][j] == 0:
                cnt += 1
    return cnt

ans = n * m

def search_cctv(number, my_map):
    global ans
    if number == len(cctvs):
        ans = min(ans, check_map(my_map))
        return
    cctv = cctvs[number]
    cctv_type = cctv[0]
    point = cctv[1], cctv[2]
    for d_list in cctv_directions[cctv_type]:
        copy_map = copy.deepcopy(my_map)
        for direction in d_list:
            check_line(point, direction, copy_map)
        
        search_cctv(number+1, copy_map)

search_cctv(0, origin_map)
print(ans)