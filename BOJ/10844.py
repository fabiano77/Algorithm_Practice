# https://www.acmicpc.net/problem/10844

'''
1: 1 2 3 4 5 6 7 8, 9
2: 10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 98 89
'''
n = int(input())
d = [[0] * (10) for _ in range(n+1)]
d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    for j in range(10):
        if j >= 1:
            d[i][j] = (d[i][j] + d[i-1][j-1]) % 1000000000
        if j <= 8:
            d[i][j] = (d[i][j] + d[i-1][j+1]) % 1000000000
print(sum(d[n])%1000000000)
