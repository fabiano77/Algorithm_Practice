import sys
import bisect
input = lambda: sys.stdin.readline().rstrip()

n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
def solve(data, c):
    start = 0
    end = data[-1] - data[0]
    ans = 0
    while start <= end:
        middle = (start+end)//2
        rightest = 0
        for _ in range(c-1):
            rightest = bisect.bisect_left(data, data[rightest]+middle, lo = rightest)
            if rightest >= len(data):
                break
        if rightest >= len(data):
            end = middle - 1
        else:
            ans = middle
            start = middle + 1
    return ans

print(solve(data, c))