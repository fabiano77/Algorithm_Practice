from itertools import combinations
n, s = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0

for num in range(1, n+1):
    for indexes in combinations(range(n), num):
        t_sum = 0
        for i in indexes:
            t_sum += data[i]
        if t_sum == s:
            cnt += 1
print(cnt)