n = int(input())
k = int(input())
data = list(map(int, input().split()))
n_cut = k-1

data.sort()
dist = []
for i in range(1, len(data)):
    distance = data[i] - data[i-1]
    if distance != 0:
        dist.append(distance)

dist.sort()
for _ in range(n_cut):
    if dist:
        dist.pop()

print(sum(dist))
'''
1  .  3  .  .  6  7  .  9
'''