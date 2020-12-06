import bisect
import sys

def search(arr, x):
    idx = bisect.bisect_left(arr,x)
    return idx < len(arr) and arr[idx] == x

N = input()
list_a = sys.stdin.readline().rstrip().split()
list_a.sort()
M = input()
list_b = sys.stdin.readline().rstrip().split()

result = str()
for item in list_b:
    if search(list_a, item): result += "1 "
    else: result += "0 "

print(result.rstrip())