from sys import stdin

input = stdin.readline

N, K = map(int, input().split())

coinType = []
for _ in range(N):
    coinType.append(int(input()))

cnt = 0

for i in range(-1, -(len(coinType)+1), -1):
    cnt += K // coinType[i]
    K %= coinType[i]

print(cnt)