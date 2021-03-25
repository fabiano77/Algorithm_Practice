import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

data = []
for _ in range(n):
    data.append(input())

a = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if data[i][j] == 'X':
            cnt = 0
        else:
            cnt += 1
        
        if cnt == 2:
            a += 1

b = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if data[j][i] == 'X':
            cnt = 0
        else:
            cnt += 1
        
        if cnt == 2:
            b += 1
        
print(a, b)