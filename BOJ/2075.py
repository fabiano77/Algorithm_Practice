import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = [[] for _ in range(n)]
pq = []
for _ in range(n):
    row = list(map(int, input().split()))
    for i in range(n):
        heapq.heappush(pq, row[i])
        if len(pq) == n+1:
            heapq.heappop(pq)
print(pq[0])