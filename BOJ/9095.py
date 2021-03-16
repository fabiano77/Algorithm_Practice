import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

def solve(n):
    global dp
    if dp[n] == 0:
        dp[n] = solve(n-1) + solve(n-2) + solve(n-3)

    return dp[n]

for _ in range(t):
    print(solve(int(input())))
