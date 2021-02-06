n = int(input())
arr = [0] + [int(input()) for _ in range(n)] + [0]
dp = [0] + [0] * (n+2)
dp[1] = arr[1]
if n >= 2:
    dp[2] = arr[1] + arr[2]
if n >= 3:
    dp[3] = arr[3] + max(arr[1], arr[2])
for i in range(4, n+2):
    dp[i] = arr[i] + max(dp[i-2], arr[i-1] + dp[i-3], arr[i-1]+dp[i-4])
print(max(dp[n], dp[n-1]))