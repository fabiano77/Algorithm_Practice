n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1
coins.sort(reverse = True)
for coin in coins:
    for i in range(1, k+1):
        if i - coin < 0:
            continue
        dp[i] += dp[i-coin]
        print(dp)
print(dp[k])
