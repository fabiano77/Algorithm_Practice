import sys
# import time
# start_time = time.time()

input = sys.stdin.readline

m, n = map(int, input().split())

mymap = []
for _ in range(n):
    mymap.append(list(map(int, input().split())))

dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

from collections import deque
def bfs(graph, queue):
    while queue:
        x, y = queue.popleft()
        day = graph[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= m-1 and (graph[nx][ny] > day + 1 or graph[nx][ny] == 0):
                queue.append([nx, ny])
                graph[nx][ny] = day + 1

def print_2d(graph):
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end = ' ')
        print()
    print()

queue = deque()
for i in range(n):
    for j in range(m):
        if mymap[i][j] == 1:
            queue.append([i, j])

bfs(mymap, queue)

max = 0
no = False
for i in range(n):
    for j in range(m):
        if mymap[i][j] == 0:
            no = True
            break
        if mymap[i][j] > max:
            max = mymap[i][j]
    if no:
        break

if no:
    print(-1)
else:
    print(max - 1)

# end_time = time.time()
# print('time = ', end_time-start_time)