n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for adjlist in graph:
    adjlist.sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for aj in graph[v]:
        if not visited[aj]:
            dfs(graph, aj, visited)

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True   # queue에 넣고 방문처리.
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for aj in graph[v]:
            if not visited[aj]:
                queue.append(aj)
                visited[aj] = True

dfs(graph, start, visited_dfs)
print()
bfs(graph, start, visited_bfs)