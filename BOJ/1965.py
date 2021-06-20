n = int(input())
li = list(map(int, input().split()))

dp = [0] * (n+1)
dp[0] = 1

for i in range(n):
    big = 0
    for j in range(i):
        if li[j] < li[i] and big < dp[j]:
            big = dp[j]
        dp[i] = big+1
print(max(dp))