import bisect
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = list(int(input()) for _ in range(n))
sorted_list = sorted(li)
ans = 0
for i in range(n-1, -1, -1):
    index = bisect.bisect_right(sorted_list, li[i]) - 1
    ans = max(ans, i - index)
print(ans + 1)