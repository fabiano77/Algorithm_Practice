import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 0
    last = 0
    people = []
    for __ in range(N):
        people.append(list(map(int,input().split())))
    people.sort()
    for person in people:
        if cnt == 0 or person[1] < last:
            cnt += 1
            last = person[1]
    print(cnt)
