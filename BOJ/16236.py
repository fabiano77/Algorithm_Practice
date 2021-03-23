import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
mymap = []
for _ in range(n):
    mymap.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if mymap[i][j] == 9:
            mymap[i][j] = 0
            start_point = (i, j)
            break

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def simulate(point):
    global n
    current_level = 2
    remain_cnt = 2
    time = 0
    searched = [[False] * n for _ in range(n)]
    cx, cy = point
    queue = deque([(cx, cy, 0)])
    searched[cx][cy] = True
    distance = 0
    while queue:
        x, y, d = queue.popleft()
        if mymap[x][y] != 0 and mymap[x][y] < current_level:
            time += d
            cd = d
            cx, cy = x, y
            while queue:
                x, y, d = queue.popleft()
                if cd == d and mymap[x][y] != 0 and mymap[x][y] < current_level:
                    if x < cx:
                        cx, cy = x, y
                    elif x == cx and y < cy:
                        cx, cy = x, y
            d = 0
            x, y = cx, cy
            mymap[cx][cy] = 0
            remain_cnt -= 1
            searched = [[False] * n for _ in range(n)]
            searched[cx][cy] = True
            if remain_cnt == 0:
                current_level += 1
                remain_cnt = current_level
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if mymap[nx][ny] > current_level:
                continue
            if searched[nx][ny]:
                continue
            queue.append((nx, ny, d+1))
            searched[nx][ny] = True
    return time

print(simulate(start_point))