import sys
input = lambda: sys.stdin.readline().rstrip()

data = []
for _ in range(5):
    data.append(input())

sol = []
for i in range(max(map(len, data))):
    for j in range(5):
        if i < len(data[j]):
            sol.append(data[j][i])

print(''.join(sol))