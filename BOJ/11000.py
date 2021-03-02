import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))

data.sort(key = lambda x: x[0])

sol = [0]

for item in data:
    if sol[0] <= item[0]:
        heapq.heappop(sol)
    heapq.heappush(sol, item[1])
    
print(len(sol))