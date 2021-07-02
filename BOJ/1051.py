n, m = map(int, input().split())
my_map = [list(map(int, input())) for _ in range(n)]
ans = 1
for i in range(n-1):
    for j in range(m-1):
        for x in range(i, n):
            for y in range(j, m):
                val = my_map[i][j]
                if my_map[i][y] == val and my_map[x][j] == val and my_map[x][y] == val:
                    ans = max(ans, (x-i+1)*(y-j+1))
print(ans)
    