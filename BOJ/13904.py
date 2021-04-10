import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
works = [ list(map(int, input().split())) for _ in range(n)]
works.sort()
pq = []
date = 1
for dead_line, point in works:
    if dead_line > date:
        while len(pq) > date:
            heapq.heappop(pq)
        while dead_line > date:    
            date += 1
    heapq.heappush(pq, point)

while len(pq) > date:
    heapq.heappop(pq)

print(sum(pq))
'''
4 60 + 2 50 + 4 40 + 3 30 + 6 5
'''