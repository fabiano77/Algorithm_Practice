import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())

# n개의 보석, k개의 가방
a = [list(map(int, input().split())) for _ in range(n)]
# 무게, 가격
b = [int(input()) for _ in range(k)]
# 가방마다 용량

a.sort()
b.sort()

pq = []

sol = 0
temp_index = 0
for bag in b:
    for index in range(temp_index, len(a)):
        if a[index][0] <= bag:
            temp_index += 1
            heapq.heappush(pq, -a[index][1])
        else:
            break
    if pq:
        sol += abs(heapq.heappop(pq))

print(sol)