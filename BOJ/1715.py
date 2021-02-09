import heapq
n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

sol = 0
while len(arr) >= 2:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    sol += a+b
    heapq.heappush(arr, a+b)

print(sol)