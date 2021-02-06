n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            lst[i][j] += lst[i-1][j]
        elif j == i:
            lst[i][j] += lst[i-1][j-1]
        else:
            lst[i][j] += max(lst[i-1][j], lst[i-1][j-1])
print(max(lst[n-1]))