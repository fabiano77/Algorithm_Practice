import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()
date = 1
idx = 0
pq = []
while idx < len(data):
    while idx < len(data) and data[idx][0] <= date:
        heapq.heappush(pq, data[idx][1])
        idx += 1
    while pq and len(pq) > date :
        heapq.heappop(pq)
    date += 1
print(sum(pq))