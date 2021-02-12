n, m = map(int, input().split())
# 1부터 n까지 자연수 중, m개를 고른 수열
# 같은 수를 여러번 골라도 됨
# 3 1 -> 1, 2, 3
# 4 2 -> 1 1, 1 2


def solve(n, depth, s):
    if depth == 0:
        print(s)
        return
    for i in range(1, n+1):
        solve(n, depth - 1, s+str(i)+' ')

solve(n, m, '')