import bisect
n = int(input()) # 크레인
cranes = list(map(int, input().split())) # 무게 제한
m = int(input()) # 박스의 수
boxes = list(map(int, input().split())) # 각 박스의 무게
cranes.sort()
boxes.sort()
crane_idx = [bisect.bisect_right(boxes, c)-1 for c in cranes]

# 1분에 박스 하나씩 배에 실을 수 있다.
# 모든 크레인은 동시에 움직인다.

if cranes[-1] < boxes[-1]:
    print(-1)
else:
    cnt = 0
    while max(boxes):
        for i in range(len(crane_idx)):
            while crane_idx[i] >= 0 and boxes[crane_idx[i]] == 0:
                crane_idx[i] -= 1
            if crane_idx[i] < 0: continue
            if boxes[crane_idx[i]]:
                boxes[crane_idx[i]] = 0
        cnt += 1
    print(cnt)

'''
3 8 15
3 5 7


7 12 15
7 5 3




'''