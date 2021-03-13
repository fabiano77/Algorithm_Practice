import sys
input = lambda: sys.stdin.readline().rstrip()

cogwheels = []
for _ in range(4):
    cogwheels.append(list(map(int, input())))
    # 12시 방향부터 8개

k = int(input())
rotations = []
for _ in range(k):
    num, rotation = map(int, input().split())
    rotations.append([num-1, rotation])
    # [0]번 톱니바퀴를 [1]이 1이면 시계, -1이면 반시계

def rotate(num, direction):
    if direction == 1:
        cogwheels[num].insert(0, cogwheels[num].pop(-1))
    else:
        cogwheels[num].append(cogwheels[num].pop(0))

def solve(num, direction):
    queue = []
    queue.append((num, direction))
    left = num-1
    left_d = direction * -1
    right = num+1
    right_d = direction * -1
    while left >= 0 or right <= 3:
        if left >= 0 and cogwheels[left+1][6] != cogwheels[left][2]:
            queue.append((left, left_d))
            left -= 1
            left_d *= -1
        else:
            left = -1

        if right <= 3 and cogwheels[right-1][2] != cogwheels[right][6]:
            queue.append((right, right_d))
            right += 1
            right_d *= -1
        else:
            right = 4
    for item in queue:
        rotate(item[0], item[1])

for item in rotations:
    solve(item[0], item[1])

ans = 0
for i in range(4):
    ans += cogwheels[i][0] * 2**i

print(ans)