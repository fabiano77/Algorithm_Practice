m = int(input())
data = list(map(int, input().split()))
n = int(input())
targets = list(map(int, input().split()))

data.sort()
import bisect
for target in targets:
    index = bisect.bisect_left(data, target)
    if index == None:
        print(0, end=' ')
    else:
        print(bisect.bisect_right(data, target)-index, end=' ')