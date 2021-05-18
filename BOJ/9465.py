'''
50  10  100 20  40
30  50  70  10  60

50  50  200 200 250
30  100 120 210 260
'''

t = int(input())
for _ in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1]+data[0][i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1]+data[1][i])
    print(max(dp[0][n-1], dp[1][n-1]))