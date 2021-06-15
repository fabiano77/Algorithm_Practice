import sys
from typing import AnyStr
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dic = {}
for _ in range(n):
    name = input()
    if name not in dic:
        dic[name] = 1
    else:
        dic[name] += 1
ans = 0
ans_name = ''
for key in dic:
    if ans < dic[key] or (ans == dic[key] and key < ans_name):
        ans = dic[key]
        ans_name = key
print(ans_name)