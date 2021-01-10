t = int(input())
for __ in range(t): 
    m, n, k = map(int, input().split())

    graph = [[0]*n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    from collections import deque
    def bfs(x, y):
        queue = deque()
        cnt = 1 # 그룹의 개수
        graph[x][y] = 2 # 방문 처리
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 제한된 영역을 벗어날 경우 스킵
                if nx <= -1 or ny <= -1 or nx >= m or ny >= n:
                    continue
                # 배추가 있는 경우만 탐색
                if graph[nx][ny] == 1:
                    cnt += 1
                    graph[nx][ny] = 2
                    queue.append((nx, ny))
        return cnt

    total = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                total += 1
    print(total)