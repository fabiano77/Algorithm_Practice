n = int(input())

arr = [0]
for _ in range(n):
    arr.append(int(input()))
'''
10  20  15  25  10  20

직전 계단을 밟는 최적값
10  30  35  50  65  65
직전 계단을 안 밟는 최적값
10  20  25  55  45  (75)
'''
d = [[0]*(n+1) for _ in range(2)]
# d[0]은 직전 계단을 밟았을 때 최적의 값
d[0][1] = arr[1]
# d[1]은 직전 계단을 안 밟았을 때 최적의 값
d[1][1] = arr[1]

for i in range(2, n+1):
    d[0][i] = arr[i] + d[1][i-1]
    d[1][i] = arr[i] + max(d[0][i-2], d[1][i-2])

print(max(d[0][n], d[1][n]))