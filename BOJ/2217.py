from sys import stdin

input = stdin.readline

N = int(input())

ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

sol = 0
cnt = 0
for rope in ropes:
    cnt += 1
    if cnt == 1:
        sol = rope
    elif sol < rope * cnt:
        sol = rope * cnt
    elif sol > N * rope:
        break

print(sol)
