dp = [0] * 31
dp[0] = 1
dp[2] = 3
n = int(input())
for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * 3
    if i >= 4:
        for j in range(4, i+1, 2):
            dp[i] += dp[i-j] * 2
print(dp[n])