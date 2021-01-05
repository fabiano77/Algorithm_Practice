import os
# 장소는 n x m 크기의 직사각형
n, m = map(int, input().split())

# 로봇청소기의 위치 r, c 그리고 방향 d(북:0, 동:1, 남:2, 서:3)
r, c, d = map(int, input().split())

# 전체 맵 입력받기 1인경우 벽, 0인경우 빈 칸.
land = []
for _ in range(n):
    land.append(list(map(int, input().split())))

# 청소한 위치를 저장하기 위한 맵 생성
clean = [[0] * m for _ in range(n)]

# 청소한 위치를 출력하는 함수
def print_map():
    global clean
    global land
    global r
    global c
    os.system('cls')
    for i in range(len(clean)):
        for j in range(len(clean[i])):
            if land[i][j] == 1:
                print('X', end=' ')
            elif i == r and j == c:
                print('A', end=' ')
            elif clean[i][j] == 0:
                print('.', end=' ')
            else:
                print('o', end=' ')
        print()

# 방향에 따른 dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 왼쪽방향 청소했는지 확인
def check_left():
    global d
    global r
    global c
    left_direction = d-1
    if left_direction == -1:
        left_direction = 3
    nx = r + dx[left_direction]
    ny = c + dy[left_direction]
    if land[nx][ny] == 0 and clean[nx][ny] == 0:
        return True
    return False

cnt = 0
turn_time = 0
#import time
# 시뮬레이션 시작
while True:
    #print_map()
    #print('청소한 칸 수 =', cnt)
    #time.sleep(0.1)
    # 1.현재 위치를 청소한다
    if clean[r][c] == 0:
        clean[r][c] = 1
        cnt += 1
    
    # 2.a 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 뱡향으로 회전한 다음, 한 칸을 전진하고 1번 진행
    if check_left() == True:
        turn_left()
        #print(r, c, '에서', r+dx[d], c+dy[d], '로 이동')
        r = r + dx[d]
        c = c + dy[d]
        turn_time = 0
        continue
    # 2.b 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    else:
        turn_left()
        turn_time += 1

    # 2.c 네 방향 모두 청소가 이미 되어있거나 벽인 경우,바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    if turn_time == 4:
        turn_time = 0
        new_d = d-2
        if new_d < 0:
            new_d + 4
        nr = r + dx[new_d]
        nc = c + dy[new_d]
        # 2.d벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다
        if land[nr][nc] == 1:
            break
        r, c = nr, nc

print(cnt)

