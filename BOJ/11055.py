n = int(input())
li = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = li[0]
for i in range(1, n):
    pre_max_index = -1
    pre_max = -1
    for j in range(0, i):
        if li[j] >= li[i]:
            continue
        elif dp[j] >= pre_max:
            pre_max = dp[j]
            pre_max_index = j
    if pre_max_index != -1:
        dp[i] = dp[pre_max_index] + li[i]
    else:
        dp[i] = li[i]
print(max(dp))