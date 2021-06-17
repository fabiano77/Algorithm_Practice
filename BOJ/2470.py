n = int(input())
li = sorted(list(map(int, input().split())))

a = 0
b = len(li)-1
ans_t = int(1e10)
ans = None
while a < b:
    t = li[a]+li[b]
    if abs(t) < ans_t:
        ans_t = abs(t)
        ans = (li[a], li[b])
    
    if t < 0:
        a += 1
    else:
        b -= 1

for item in ans:
    print(item, end=' ')