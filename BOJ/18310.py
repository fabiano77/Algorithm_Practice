from collections import Counter
n = int(input())
data = list(map(int, input().split()))
counter = Counter(data)
total_d = sum(data)
min_d = total_d
left_side = 0
ans = 0
for i in range(1, 100001):
    right_side = n - left_side
    total_d += left_side
    total_d -= right_side
    if min_d > total_d:
        min_d = total_d
        ans = i
    else:
        break
    left_side += counter[i]

print(ans)


