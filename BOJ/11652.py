from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()

a = {}
for _ in range(int(input())):
    s = input()
    if s in a:
        a[s] += 1
    else:
        a[s] = 1

max_v = False
max_k = 0
for key in a.keys():
    if max_v == False:
        max_v = int(a[key])
        max_k = key
    elif max_v < int(a[key]) or (max_v == int(a[key]) and int(max_k) > int(key)) :
        max_v = int(a[key])
        max_k = key

print(max_k)