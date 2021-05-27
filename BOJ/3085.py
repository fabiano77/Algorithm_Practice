import sys
import copy
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
my_map = [list(input()) for _ in range(n)]

def solve(my_map):
    global n
    cnt = 0
    for i in range(n):
        a_cnt = 1
        b_cnt = 1
        for j in range(1, n):
            if my_map[i][j] == my_map[i][j-1]:
                a_cnt += 1
            else:
                a_cnt = 1
            if my_map[j][i] == my_map[j-1][i]:
                b_cnt += 1
            else:
                b_cnt = 1
            cnt = max(cnt, a_cnt, b_cnt)
    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        cp = copy.deepcopy(my_map)
        if i+1 < n:
            cp[i][j], cp[i+1][j] = cp[i+1][j], cp[i][j]
            ans = max(solve(cp), ans)

        cp = copy.deepcopy(my_map)
        if j+1 < n:
            cp[i][j], cp[i][j+1] = cp[i][j+1], cp[i][j]
            ans = max(solve(cp), ans)
print(ans)