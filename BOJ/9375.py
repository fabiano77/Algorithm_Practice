import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    item = {}
    for _ in range(n):
        data = list(input().split())
        if data[1] in item:
            item[data[1]] += 1
        else:
            item[data[1]] = 1
    num_list = []
    ans = 1
    for i in item.keys():
        ans *= (item[i] + 1)
    print(ans-1)