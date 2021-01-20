k = int(input())

arr = []
for _ in range(k):
    t = int(input())
    if t == 0:
        arr.pop()
    else:
        arr.append(t)

print(sum(arr))