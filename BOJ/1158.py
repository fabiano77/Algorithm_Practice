from collections import deque
n, k = map(int, input().split())
q = deque(range(1, n+1))
ans = []
order = 1
while q:
    item = q.popleft()
    if order == k:
        ans.append(str(item))
        order = 1
    else:
        q.append(item)
        order += 1
print(f"<{', '.join(ans)}>")


