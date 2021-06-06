'''
1,
10
100, 101
1001, 1000, 1010
10010, 10000, 10001, 10100, 10101
'''
n = int(input())
last_1 = [0] * (n+1)
last_0 = [0] * (n+1)
last_1[1] = 1
for i in range(2, n+1):
    last_1[i] = last_0[i-1]
    last_0[i] = last_0[i-1] + last_1[i-1]
print(last_1[n]+last_0[n])