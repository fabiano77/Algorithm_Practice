n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]

TF = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j] == B[i][j])
    TF.append(row)

def flip_3by3(x, y):
    for i in range(3):
        for j in range(3):
            TF[x+i][y+j] = not TF[x+i][y+j]

def check():
    for i in range(n):
        for j in range(m):
            if not TF[i][j]:
                return False
    return True
cnt = 0
for i in range(n-2): # 3 -> 0, 1, 2 
    for j in range(m-2):
        if not TF[i][j]:
            flip_3by3(i, j)
            cnt += 1

if check():
    print(cnt)
else:
    print(-1)
