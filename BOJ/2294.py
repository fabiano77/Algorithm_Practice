import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [-1] * (k+1)
dp[0] = 0

for i in range(1, k+1):
    for coin in coins:
        if i - coin >= 0 and dp[i-coin]>=0:
            if dp[i] == -1:
                if dp[i-coin] == -1:
                    continue
                else:
                    dp[i] = dp[i-coin]+1
            else:
                dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[k])