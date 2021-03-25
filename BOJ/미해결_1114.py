import heapq
import random

#length, pos_len, cut_times = map(int, input().split())
length = random.randint(1, 100)
pos_len = random.randint(1, length)
cut_times = random.randint(1, pos_len)

positions = list(random.sample(range(1, length),  pos_len))

print(length, pos_len, cut_times)

print(positions)


# l은 통나무의 길이
# k는 자를 수 있는 위치의 개수
# c은 자를 수 있는 쵯수

#positions = list(map(int, input().split()))
positions.sort()
# 자를 수 있는 위치 정보

if len(positions) < cut_times: cut_times = len(positions)

log = (-(length-0), 0, length)
# 통나무: (-길이, 시작점, 끝점)
lst = []
heapq.heappush(lst, log)
# 통나무 리스트

existence = True
first_sel = True
first_pos = -1

while cut_times:
    cut_times -= 1

    # 가장 긴 통나무의 처음과 끝 좌표를 start, end로 함
    start = lst[0][1]
    end = lst[0][2]

    # 자를 수 있는 위치들을 이분탐색하기 위한 index 변수
    first_idx = 0
    last_idx = len(positions)-1

    # 최종적으로 이분탐색한 결과를 담을 sol_idx 변수
    sol_idx = -1

    # 가장 작을 수 있는 자른 통나무중 긴 것의 길이 변수
    # 에 현재 통나무의 길이를 담음
    shortest_long_part = abs(lst[0][0])

    # 현재 통나무에 자를 수 있는 위치가 있는가?
    existence = False

    while first_idx <= last_idx:
        middle_idx = (first_idx + last_idx)//2

        # 자를 위치가 현재 통나무 밖일 경우
        if positions[middle_idx] <= start:
            first_idx = middle_idx + 1
            continue
        elif positions[middle_idx] >= end:
            last_idx = middle_idx - 1
            continue

        # 자를 수 있는 위치가 현재 통나무에 존재
        existence = True

        if positions[middle_idx] - start < end - positions[middle_idx]:
            # 왼쪽 길이가 더 작을 경우
            long_part = end - positions[middle_idx]
            first_idx = middle_idx + 1
        else:
            # 오른 쪽 길이가 더 작거나 같은 경우
            long_part = positions[middle_idx] - start
            last_idx = middle_idx - 1

        # print(f'first_idx = {first_idx}, last_idx = {last_idx}, middle_idx = {middle_idx}')
        # print(f's_l_p = {shortest_long_part}, long_part = {long_part}')
        # 현재 자른 위치의 긴 부분이 작아질 수 있는 경우
        if shortest_long_part > long_part or (shortest_long_part == long_part and sol_idx > middle_idx):
            shortest_long_part = long_part
            sol_idx = middle_idx
            if first_sel:
                first_pos = positions[middle_idx]

    first_sel = False

    if existence:
        # 가장 긴 통나무를 리스트에서 빼내고
        log = heapq.heappop(lst)
        # 위에서 도출한 값으로 통나무를 두개로 자름
        log_left = (-(positions[sol_idx] - start), start, positions[sol_idx])
        log_right = (-(end - positions[sol_idx]), positions[sol_idx], end)
        # heap구조로 가장 길이가 긴 통나무를 lst[0]에 오게 함
        heapq.heappush(lst, log_left)
        heapq.heappush(lst, log_right)
    else:
        # 가장 긴 통나무에 자를 수 있는 위치가 없는 경우 반복종료
        break
    print(lst)

print(abs(lst[0][0]), first_pos)

'''

0  1  2  3, 4, 5, 6  7  8, 9, 10 11 12,13 14 15,16,17 18 19,20


문제점: 3번 커팅할 시, 3등분되지않음.

'''