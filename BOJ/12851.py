from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001
def bfs(n, k):
    t = 0
    ans_cnt = 0
    ans_t = 100000
    queue = deque([[n, t]])
    visited[n] = True

    while queue:
        n, t = queue.popleft()
        if t > ans_t:
            break
        if n == k:
            ans_cnt += 1
            ans_t = t
        else:
            t += 1
            if n-1 >= 0 and visited[n-1] < 5:
                queue.append([n-1, t])
            if n+1 <= 100000 and visited[n+1] < 5:
                queue.append([n+1, t])
            if 2*n <= 100000 and visited[2*n] < 5:
                queue.append([2*n, t])
            if n-1 >= 0 and n-1 != k: 
                visited[n-1] += 1
            if n+1 <= 100000 and n+1 != k: 
                visited[n+1] += 1
            if 2*n <= 100000 and 2*n != k: 
                visited[2*n] += 1

    return ans_t, ans_cnt

t, cnt = bfs(n, k)
print(t)
print(cnt)