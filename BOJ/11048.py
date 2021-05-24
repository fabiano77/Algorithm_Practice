n, m = map(int, input().split())

my_map = []
for _ in range(n):
    my_map.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if i == 0:
            if j == 0:
                continue
            else:
                my_map[i][j] += my_map[i][j-1]
        else:
            if j == 0:
                my_map[i][j] += my_map[i-1][j]
            else:
                my_map[i][j] += max(my_map[i-1][j], my_map[i][j-1])

print(my_map[n-1][m-1])