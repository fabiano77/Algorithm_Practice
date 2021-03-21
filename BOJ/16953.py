a, b = map(int, input().split())

from collections import deque
def solve(a):
    global b
    target = b
    queue = deque([a])
    cnt = 1
    while queue:
        for _ in range(len(queue)):
            item = queue.popleft()
            if item == target:
                return cnt
            if item > target:
                continue
            queue.append(item*2)
            queue.append(item*10 + 1)
        cnt += 1
    return -1
        
print(solve(a))