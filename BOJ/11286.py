import heapq
import sys
input = sys.stdin.readline

priorityQ = []
for _ in range(int(input())):
    data = int(input())

    if data == 0:
        if priorityQ:
            print(heapq.heappop(priorityQ)[1])
        else:
            print(0)
    else:
        heapq.heappush(priorityQ, (abs(data), data))
