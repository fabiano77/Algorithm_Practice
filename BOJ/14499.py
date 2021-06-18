n, m, x, y, k = map(int, input().split())
# n, m 지도의 크기
# x, y 주사위의 위치
# k 이동 횟수
my_map = []
for _ in range(n):
    my_map.append(list(map(int, input().split())))
orders = list(map(int, input().split()))

dice = [0] * 6
'''
   3
5  0  4
   1
   2
'''
def dice_roll(direction):
    if direction == 1: # east
        dice[0], dice[4], dice[2], dice[5] = dice[5], dice[0], dice[4], dice[2]
    elif direction == 2:
        dice[0], dice[4], dice[2], dice[5] = dice[4], dice[2], dice[5], dice[0]
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif direction == 4:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for d in orders:
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    x, y = nx, ny
    dice_roll(d)
    if my_map[x][y] == 0:
        my_map[x][y] = dice[2]
    else:
        dice[2] = my_map[x][y]
        my_map[x][y] = 0
    print(dice[0])