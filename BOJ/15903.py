import heapq
n, m = map(int, input().split())
pq = list(map(int, input().split()))
heapq.heapify(pq)

for _ in range(m):
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    c = a + b
    for _ in range(2): heapq.heappush(pq, c)
print(sum(pq))