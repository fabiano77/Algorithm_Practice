
dp = [[0] * 31 for _ in range(31)]
def comb(n, r):
    if dp[n][r] != 0:
        return dp[n][r]
    if n == r or r == 0:
        return 1
    dp[n][r] = comb(n-1, r-1) + comb(n-1, r)
    return dp[n][r]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(comb(m, n))
