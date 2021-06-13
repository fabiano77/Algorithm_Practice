n = int(input())
li = list(map(int, input().split()))

from itertools import permutations

ans = -1

for orders in permutations(range(n), n):
    temp = 0
    for i in range(n-1):
        temp += abs(li[orders[i]] - li[orders[i+1]])
    ans = max(ans, temp)
print(ans)
