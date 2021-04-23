import sys
input = lambda: sys.stdin.readline().rstrip()

n, c = map(int, input().split())
m = int(input())
data = [list(map(int, input().split()))for _ in range(m)]
#data.sort(key = lambda x:(x[1]-x[0], x[1]))
data.sort(key = lambda x:(x[1], x[1]-x[0]))
for i in data:
    print(i)
truck_in_town_of = [0]*2001
ans = 0

for start, end, point in data:
    allowed_box = min(c - max(truck_in_town_of[start:end]), point)
    for i in range(start, end):
        truck_in_town_of[i] += allowed_box
    ans += allowed_box
    print(f'ans += box : {ans} += {allowed_box}')

print(ans)