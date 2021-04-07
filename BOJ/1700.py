n, k = map(int, input().split())
data = list(map(int, input().split()))
data = [[item, -100] for item in data]
ans = 0
exist = [False]*101
next_index = [-100]*101
for i in range(len(data)-1, -1, -1):
    if next_index[data[i][0]] != -100:
        data[i][1] = next_index[data[i][0]]
    next_index[data[i][0]] = -i
    
import heapq
import bisect
p_queue = []

for item in data:
    name, next_idx = item
    if exist[name]:
        idx = 0
        for i in range(len(p_queue)):
            idx = i
            if p_queue[i][1] == name:
                break
        p_queue[idx][0] = next_idx
        heapq.heapify(p_queue)
        continue
    if len(p_queue) >= n:
        out_item = heapq.heappop(p_queue)
        exist[out_item[1]] = False
        ans += 1
    heapq.heappush(p_queue, [next_idx, name])
    exist[name] = True

print(ans)