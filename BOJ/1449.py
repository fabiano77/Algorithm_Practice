import sys

input = sys.stdin.readline

N, L = map(int, input().split())

pipes = list(map(int, input().split()))

pipes.sort()
last_position = 0
cnt = 0
for pipe in pipes:
    if pipe <= last_position:
        pass
    else:
        last_position = pipe + (L-1)
        cnt += 1

print(cnt)