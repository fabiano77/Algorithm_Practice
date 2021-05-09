import sys
sys.setrecursionlimit(10000000)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
sol = [[0] * n for _ in range(n)]

def solve(start_v):
    global n
    for i in range(n):
        if mat[start_v][i] == 1 and sol[start_v][i] == 0:
            sol[start_v][i] = 1
            for j in range(n):
                if mat[start_v][j] == 0 and mat[i][j] == 1:
                    mat[start_v][j] = 1
            solve(i)

for i in range(n):
    solve(i)

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()
