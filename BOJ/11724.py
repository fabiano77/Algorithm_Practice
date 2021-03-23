import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n+1)

def dfs(graph, v, visited):
    stack = []
    stack.append(v)
    visited[v] = True
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if not visited[nv]:
                stack.append(nv)
                visited[nv] = True
    return 1

cnt = 0     
for i in range(1, n+1):
    if not visited[i]:
        cnt += dfs(graph, i, visited)
print(cnt)