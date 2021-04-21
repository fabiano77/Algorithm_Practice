import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
data = [int(input()) for _ in range(n)]
ans = 0
for i in range(len(data) - 2, -1, -1):
    if data[i] >= data[i+1]:
        ans += (data[i] - data[i+1] + 1)
        data[i] = data[i+1] - 1
print(ans)


'''
6 -> 2
5 -> 3
4
8

'''