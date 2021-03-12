import sys
sys.setrecursionlimit(100000)

n, k = map(int, input().split())

dp = [[-1]*(k+1) for _ in range(n+1)]

def bin(n, k):
    if k == 0 or k == n:
        return 1
    if dp[n-1][k-1] == -1:
        dp[n-1][k-1] = bin(n-1, k-1)
    if dp[n-1][k] == -1:
        dp[n-1][k] = bin(n-1, k)

    return (dp[n-1][k-1] + dp[n-1][k])%10007

print(bin(n, k))