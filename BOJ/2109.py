import heapq
n = int(input())
li = []
ans = 0
for _ in range(n):
    p, d = map(int, input().split())
    heapq.heappush(li, (d, -p))
box = []
while li:
    d, p = heapq.heappop(li)
    p = -p
    if len(box) < d:
        ans += p
        heapq.heappush(box, p)
    elif box[0] < p:
        ans -= box[0]
        ans += p
        heapq.heappop(box)
        heapq.heappush(box, p)
print(ans)