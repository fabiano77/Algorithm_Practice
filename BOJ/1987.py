n, c = map(int, input().split())
mymap = [input() for _ in range(n)]

dx = [+1, 0, -1, 0]
dy = [0, +1, 0, -1]
def dfs(point):
    x, y = point
    stack = [[point, mymap[x][y]]]
    longest = 0
    while stack:
        print(stack)
        point, history = stack.pop()
        longest = max(longest, len(history))
        x, y = point
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= c:
                continue
            if mymap[nx][ny] in history: 
                continue
            next_point = (nx, ny)
            next_history = history + mymap[nx][ny]
            stack.append([next_point, next_history])
    return longest

print(dfs((0, 0)))

