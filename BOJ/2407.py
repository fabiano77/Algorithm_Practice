n, m = map(int, input().split())

dp = [[0] * 101 for _ in range(101)]

def comb(n, r):
    if dp[n][r] != 0:
        return dp[n][r]
    if n == r or r == 0:
        return 1
    dp[n][r] = comb(n-1, r-1) + comb(n-1, r)
    return dp[n][r]
print(comb(n, m))