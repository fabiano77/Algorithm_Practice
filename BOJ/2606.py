n = int(input())
e = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for adjList in graph:
    adjList.sort()

visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    for adj in graph[v]:
        if not visited[adj]:
            dfs(graph, adj, visited)

dfs(graph, 1, visited)

cnt = 0
for i in visited:
    if i == True:
        cnt+=1
print(cnt-1)