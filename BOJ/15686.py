import sys
from collections import deque
import itertools

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

houses = [(i, j) for i in range(n) for j in range(n) if data[i][j] == 1]
chicken_restaurants = [(i, j) for i in range(n) for j in range(n) if data[i][j] == 2]

def solve(houses, chickens):
    global n
    distances = [2*n] * len(houses)
    for point in chickens:
        for i, house in enumerate(houses):
            distances[i] = min(distances[i], abs(point[0]-house[0]) + abs(point[1]-house[1]))
    return sum(distances)


def update_distances(houses, point):
    global distances

    return distances

best = 2*n*n*n

for case in itertools.combinations(chicken_restaurants, m):
    best = min(best, solve(houses, case))

print(best)