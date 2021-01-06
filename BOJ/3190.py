# 게임은 n * n 의 정사각 보드에서 진행
n = int(input())
land = [[0] * n for _ in range(n)]
apples = [[0] * n for _ in range(n)]

def print_2d_map(mat):
    for li in mat:
        for ch in li:
            print(ch, end=' ')
        print()

# k개의 사과가 존재한다.
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    apples[x-1][y-1] = 1

# 뱀의 방향 변환 횟수 l이 주어짐.
l = int(input())
controls = []
for _ in range(l):
    x, c = input().split()
    x = int(x)
    controls.append([x, c])

# 4가지 방향 북:0, 동:1, 남:2, 서:3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 뱀의 몸통 길이 시작은 1
leng = 1

# 방향: 동; 시작위치: 0, 0 설정
direction = 1
x, y = 0, 0
body = [[x, y]]
land[x][y] = 1
time = 0

# 좌, 우로 방향을 회전하는 함수.
def turn(c):
    global direction
    if c == 'L':
        direction -= 1
        if direction < 0:
            direction = 3
    elif c == 'D':
        direction += 1
        if direction > 3:
            direction = 0

cnt_apple = 0
# 시뮬레이션 시작
while True:
    # 뱀의 방향 변환 정보
    if len(controls) > 0 and controls[0][0] == time:
        turn(controls[0][1])
        controls.pop(0)

    nx = x + dx[direction]
    ny = y + dy[direction]
    # 몸에 부딛히거나 맵 밖으로나갈경우 게임 종료
    if  nx < 0 or nx >= n or ny < 0 or ny >= n or land[nx][ny] == 1 :
        print(time+1)
        break

    # 사과를 먹을 경우, 몸 길이가 1 늘어남.
    if apples[nx][ny] == 1:
        apples[nx][ny] = 0
        cnt_apple += 1
    else:
        del_body = body.pop(0)
        land[del_body[0]][del_body[1]] = 0

    x, y = nx, ny
    land[x][y] = 1
    body.append([x, y])

    time += 1