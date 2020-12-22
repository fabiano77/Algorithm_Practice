import sys
import bisect

N = int(input())

arr = list(map(int, input().split()))

new = []
n_len = 0

for i in arr:
    index = bisect.bisect_left(new, i)

    if len(new) <= index:
        new.append(i)
    else:
        new[index] = i

print(len(new))


