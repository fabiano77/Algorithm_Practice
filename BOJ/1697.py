from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001
def bfs(n, k):
    t = 0
    queue = deque([[n, t]])
    visited[n] = True

    while queue:
        n, t = queue.popleft()
        if n == k:
            break
        t += 1
        if n-1 >= 0 and not visited[n-1]:
            queue.append([n-1, t])
            visited[n-1] = True
        if n+1 <= 100000 and not visited[n+1]:
            queue.append([n+1, t])
            visited[n+1] = True
        if 2*n <= 100000 and not visited[2*n]:
            queue.append([2*n, t])
            visited[2*n] = True

    return t

print(bfs(n, k))