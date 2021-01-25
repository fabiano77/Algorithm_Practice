import sys

n, m = map(int, input().split())

origin = []
for _ in range(n):
    origin.append(list(map(int, input().split())))
# graph = [[0] * m for _ in range(n)]

new_wall = [[0, 0], [0, 1], [0, 2]]

def print_2d(graph):
    global new_wall
    print()
    for i in range(n):
        for j in range(m):
            is_new_wall = False
            for k in range(3):
                if i == new_wall[k][0] and j == new_wall[k][1]:
                    print(3, end = ' ')
                    is_new_wall = True
            if not is_new_wall:
                print(graph[i][j], end = ' ')
        print()
    print()

direction = [0, 1, 2, 3]
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]
# print_2d()


def next_new_wall():
    global origin
    global new_wall

    while True:
        new_wall[2][1] += 1     # 3번째 임의벽 다음 열
        check_flag = True

        while check_flag:
            check_flag = False

            if new_wall[2][1] >= m: # 3번째 임의벽 다음 행
                new_wall[2][1] = 0
                new_wall[2][0] += 1
                check_flag = True
            
            if new_wall[2][0] >= n: # 2번째 임의벽 다음 열 
                new_wall[1][1] += 1

                new_wall[2][0] = new_wall[1][0]
                new_wall[2][1] = new_wall[1][1] + 1
                check_flag = True

            if new_wall[1][1] >= m: # 2번째 임의벽 다음 행
                new_wall[1][1] = 0
                new_wall[1][0] += 1

                new_wall[2][0] = new_wall[1][0]
                new_wall[2][1] = new_wall[1][1] + 1
                check_flag = True

            if new_wall[1][0] >= n: # 1번째 임의벽 다음 열
                new_wall[0][1] += 1

                new_wall[1][0] = new_wall[0][0]
                new_wall[1][1] = new_wall[0][1] + 1
                new_wall[2][0] = new_wall[1][0]
                new_wall[2][1] = new_wall[1][1] + 1
                check_flag = True
            
            if new_wall[0][1] >= m: # 1번째 임의벽 다음 행
                new_wall[0][1] = 0
                new_wall[0][0] += 1
                
                new_wall[1][0] = new_wall[0][0]
                new_wall[1][1] = new_wall[0][1] + 1
                new_wall[2][0] = new_wall[1][0]
                new_wall[2][1] = new_wall[1][1] + 1
                check_flag = True

            if new_wall[0][0] >= n:
                return False

        for i in range(4):
            if i == 3:
                return True 
            x, y = new_wall[i]
            if origin[x][y] != 0:    # new_wall의 위치가 0이 아니라 1, 2일 경우 break하여 재실행
                break

def set_new_wall():
    while True:
        for i in range(4):
            if i == 3:
                return
            x, y = new_wall[i]
            if origin[x][y] == 1 or origin[x][y] == 2:
                next_new_wall()
                break

from collections import deque
def bfs(graph, queue):
    global new_wall
    global n, m
    queue = deque(queue)
    visited = [[False] * m for _ in range(n)]
    for item in queue:
        visited[item[0]][item[1]] = True
    cnt_virus = len(queue)
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0 and not visited[nx][ny] and [nx, ny] not in new_wall:
                queue.append([nx, ny])
                cnt_virus += 1
                visited[nx][ny] = True
    return cnt_virus

# import os
# import time
min_virus = n*m
wall_cnt = 0
set_new_wall()  # 임의벽 초기화
virus = []      # 바이러스 칸 수집
for i in range(n):
    for j in range(m):
        if origin[i][j] == 2:
            virus.append([i, j])
        elif origin[i][j] == 1:
            wall_cnt += 1

while True:           # 시뮬레이션 시작
    # os.system('cls')  # 콘솔 지우기
    # print_2d(origin)

    v_cnt = bfs(origin, virus)
    if v_cnt < min_virus:
        min_virus = v_cnt
        
    # time.sleep(0.01)
    if next_new_wall() == False:
        break

print(n*m - wall_cnt - min_virus - len(new_wall))