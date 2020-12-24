coinType = [500, 100, 50, 10, 5, 1]

N = int(input())
N = 1000 - N
cnt = 0
for coin in coinType:
    cnt += N//coin
    N = N%coin

print(cnt)