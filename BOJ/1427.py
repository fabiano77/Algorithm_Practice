import sys
input = sys.stdin.readline

N = input().rstrip()

M = sorted(N,reverse=True)

for i in M:
    print(int(i),end='')


