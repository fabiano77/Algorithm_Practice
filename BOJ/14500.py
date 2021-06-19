n, m = map(int, input().split())
my_map = []
for _ in range(n):
    my_map.append(list(map(int, input().split())))

tetrominos = [  [(0, 0), (0, 1), (0, 2), (0, 3)],
                [(0, 0), (0, 1), (1, 0), (1, 1)],
                [(0, 0), (1, 0), (2, 0), (2, 1)],
                [(0, 0), (1, 0), (1, 1), (2, 1)],
                [(0, 0), (0, 1), (0, 2), (1, 1)],
                ]

# 회전변환 
'''
(0 -1)
(1  0)
'''
def rotation(tetromino):
    for i in range(len(tetromino)):
        x, y = tetromino[i]
        tetromino[i] = (y, -x)

def symmetry(tetromino):
    for i in range(len(tetromino)):
        x, y = tetromino[i]
        tetromino[i] = (x, -y)

ans = 0
for x in range(n):
    for y in range(m):
        for tetromino in tetrominos:
            for _ in range(2):
                symmetry(tetromino)
                for _ in range(4):
                    rotation(tetromino)
                    temp_point = 0
                    out_of_here = False
                    for dx, dy in tetromino:
                        nx = x + dx
                        ny = y + dy
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            out_of_here = True
                            break
                        temp_point += my_map[nx][ny]
                    if out_of_here:
                        continue
                    ans = max(ans, temp_point)

print(ans)
            
