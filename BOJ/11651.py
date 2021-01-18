n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])

points.sort(key = lambda x: x[0])
points.sort(key = lambda y: y[1])

for point in points:
    print(point[0], point[1])