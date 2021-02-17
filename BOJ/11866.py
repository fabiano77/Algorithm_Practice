from collections import deque
n, k = map(int, input().split())

q = deque(range(1, n+1))

lst = []

while q:
    for i in range(k):
        item = q.popleft()
        if i == k-1:
            lst.append(item)
        else:
            q.append(item)

print('<', end='')
for index, num in enumerate(lst):
    if index == len(lst)-1:
        print(num, end='>\n')
    else:
        print(num, end=', ')