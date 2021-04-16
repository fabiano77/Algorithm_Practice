li = []
for i in range(1, 46):
    for _ in range(i):
        li.append(i)
a, b = map(int, input().split())
print(sum(li[a-1:b]))