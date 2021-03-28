import sys
input = lambda: sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())

li = [a, b, c]
li.sort()
for i in li:
    print(i, end = ' ')