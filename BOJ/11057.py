import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

dp = [[0] for _ in range(10)]
for i in range(10):
    dp[i].append(1)

for i in range(2, n+1): # n에 대응
    for j in range(10): # 0~9에 대응
        temp = 0
        for k in range(0, j+1): #0부터 j까지 대응
            temp = (temp + dp[k][i-1])%10007
        dp[j].append(temp)

sol = 0
for i in range(10):
    sol = (sol + dp[i][n])%10007

print(sol)


'''

[1]
1 2 3 4 5 6 7 8 9 0
=> 10

[2]
00 11 22 33 44 55 66 77 88 99

0(9)
1(8)
2(7)
3(6)
4(5)
6(4)
7(3)
8(2)
9(1)



'''